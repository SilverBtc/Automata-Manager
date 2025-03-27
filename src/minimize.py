from collections import defaultdict
from FiniteAutomata import FiniteAutomata

def minimize(fa):
    def group_name(group):
        return '.'.join(map(str, sorted(group)))

    # Étape 1 : créer les partitions initiales (finales vs non-finales)
    partitions = set()
    non_final = frozenset(fa.states - fa.final_states)
    final = frozenset(fa.final_states)
    if final:
        partitions.add(final)
    if non_final:
        partitions.add(non_final)

    # Étape 2 : Raffiner les partitions
    while True:
        new_partitions = set()
        for group in partitions:
            split = defaultdict(set)
            for state in group:
                # Signature = vers quelles partitions pointent les transitions
                key = tuple()
                for sym in sorted(fa.alphabet):
                    tgt = next(iter(fa.get_transitions(state, sym)), None)
                    for p in partitions:
                        if tgt in p:
                            key += (frozenset(p),)
                            break
                split[key].add(state)
            for s in split.values():
                new_partitions.add(frozenset(s))
        if new_partitions == partitions:
            break
        partitions = new_partitions

    # Étape 3 : Création de l'automate minimal
    state_to_group = {}
    for group in partitions:
        for state in group:
            state_to_group[state] = group

    new_fa = FiniteAutomata()
    new_fa.alphabet = fa.alphabet.copy()
    new_fa.states = {group_name(group) for group in partitions}

    init_group = state_to_group[next(iter(fa.initial_states))]
    new_fa.initial_states = {group_name(init_group)}

    new_fa.final_states = {
        group_name(group) for group in partitions if group & fa.final_states
    }

    for group in partitions:
        rep_state = next(iter(group))
        for sym in fa.alphabet:
            tgts = fa.get_transitions(rep_state, sym)
            if tgts:
                tgt = next(iter(tgts))
                tgt_group = state_to_group[tgt]
                new_fa.add_transition(group_name(group), sym, group_name(tgt_group))

    return new_fa
