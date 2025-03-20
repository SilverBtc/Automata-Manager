# Check if FA is complete
def is_complete(fa):
    for state in fa.states:
        for symbol in fa.alphabet:
            if len(fa.get_transitions(state, symbol)) != 1:
                return False, f"State {state} missing transition for {symbol}."
    return True, "FA is complete."