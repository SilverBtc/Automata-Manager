
# Check if FA is deterministic
def is_deterministic(fa):
    if len(fa.initial_states) != 1:
        return False, "Multiple initial states."
    for state in fa.states:
        for symbol in fa.alphabet:
            if len(fa.get_transitions(state, symbol)) > 1:
                return False, f"State {state} has multiple transitions for {symbol}."
    return True, "FA is deterministic."