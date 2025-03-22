from collections import defaultdict
from FiniteAutomata import FiniteAutomata


def minimize(fa):
    # Hopcroft's algorithm (simplified)
    partitions = set()
    non_final = frozenset(fa.states - fa.final_states)
    final = frozenset(fa.final_states)
    if final:
        partitions.add(final)
    if non_final:
        partitions.add(non_final)
    while True:
        new_partitions = set()
        for group in partitions:
            split = defaultdict(set)
            for state in group:
                key = tuple()
                for sym in sorted(fa.alphabet):
                    tgt = next(iter(fa.get_transitions(state, sym)), None)
                    for p in partitions:
                        if tgt in p:
                            key += (p,)
                            break
                split[key].add(state)
            for s in split.values():
                new_partitions.add(frozenset(s))
        if new_partitions == partitions:
            break
        partitions = new_partitions
    state_to_group = {}
    for group in partitions:
        for state in group:
            state_to_group[state] = group
    new_states = partitions
    new_initial = next(iter(state_to_group[next(iter(fa.initial_states))]))
    new_final = set()
    for group in partitions:
        if any(s in fa.final_states for s in group):
            new_final.add(group)
    new_fa = FiniteAutomata()
    new_fa.alphabet = fa.alphabet.copy()
    new_fa.initial_states = {str(new_initial)}
    new_fa.final_states = {str(g) for g in new_final}
    new_fa.states = {str(g) for g in partitions}
    for group in partitions:
        for sym in fa.alphabet:
            tgt_state = next(iter(fa.get_transitions(next(iter(group)), sym)))
            tgt_group = state_to_group[tgt_state]
            new_fa.add_transition(str(group), sym, str(tgt_group))
    return new_fa
