from FiniteAutomata import FiniteAutomata

def complete(fa):
    sink = 'sink'
    new_fa = FiniteAutomata()
    new_fa.alphabet = fa.alphabet.copy()
    new_fa.states = fa.states.copy()
    if sink not in new_fa.states:
        new_fa.states.add(sink)
    new_fa.initial_states = fa.initial_states.copy()
    new_fa.final_states = fa.final_states.copy()
    for src in fa.transitions:
        for sym in fa.alphabet:
            tgts = fa.get_transitions(src, sym)
            if tgts:
                new_fa.transitions[src][sym] = tgts.copy()
            else:
                new_fa.add_transition(src, sym, sink)
    for sym in new_fa.alphabet:
        new_fa.add_transition(sink, sym, sink)
    return new_fa