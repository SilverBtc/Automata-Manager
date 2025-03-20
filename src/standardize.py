from FiniteAutomata import FiniteAutomata
from src.is_standard import is_standard

def standardize(fa):
    is_std, msg = is_standard(fa)
    if is_std:
        return fa, "Already standard."
    new_initial = max(fa.states) + 1 if fa.states else 0
    new_fa = FiniteAutomata()
    new_fa.alphabet = fa.alphabet.copy()
    new_fa.states = fa.states.copy()
    new_fa.states.add(new_initial)
    new_fa.initial_states = {new_initial}
    new_fa.final_states = fa.final_states.copy()
    for src in fa.transitions:
        for sym in fa.transitions[src]:
            for tgt in fa.transitions[src][sym]:
                new_fa.add_transition(src, sym, tgt)
    for old_init in fa.initial_states:
        for sym in fa.alphabet:
            tgts = fa.get_transitions(old_init, sym)
            for tgt in tgts:
                new_fa.add_transition(new_initial, sym, tgt)
    return new_fa, "Standardized by adding new initial state."