def is_standard(fa):
    if len(fa.initial_states) != 1:
        return False, "Multiple initial states."
    initial = next(iter(fa.initial_states))
    for state in fa.states:
        for symbol in fa.alphabet:
            if initial in fa.get_transitions(state, symbol):
                return False, f"Initial state {initial} has incoming transition from {state} on {symbol}."
    return True, "FA is standard."