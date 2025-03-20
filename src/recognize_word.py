def recognize_word(word, fa):
    current = fa.initial_states
    for sym in word:
        next_states = set()
        for state in current:
            next_states.update(fa.get_transitions(state, sym))
        if not next_states:
            return False
        current = next_states
    return any(state in fa.final_states for state in current)