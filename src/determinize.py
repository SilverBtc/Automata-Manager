from collections import defaultdict
from FiniteAutomata import FiniteAutomata

def determinize(fa):
    initial = frozenset(fa.initial_states)
    pending = [initial]
    states = set()
    transitions = defaultdict(dict)
    finals = set()

    while pending:
        current = pending.pop()
        if current in states:
            continue
        states.add(current)
        if any(s in fa.final_states for s in current):
            finals.add(current)
        for sym in fa.alphabet:
            next_states = set()
            for s in current:
                next_states.update(fa.get_transitions(s, sym))
            next_frozen = frozenset(next_states)
            transitions[current][sym] = next_frozen
            if next_frozen not in states:
                pending.append(next_frozen)
    new_fa = FiniteAutomata()
    new_fa.alphabet = fa.alphabet.copy()
    state_map = {s: '.'.join(sorted(map(str, s))) for s in states}
    new_fa.states = set(state_map.values())
    new_fa.initial_states = {state_map[initial]}
    new_fa.final_states = {state_map[s] for s in finals}
    for src, syms in transitions.items():
        for sym, tgt in syms.items():
            new_fa.add_transition(state_map[src], sym, state_map[tgt])
    return new_fa
