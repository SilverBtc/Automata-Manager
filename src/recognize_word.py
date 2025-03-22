def recognize_word(fa, word):
    try:
        current = fa.initial_states
    except AttributeError:
        current = fa.get('initial_states', set())

    for sym in word:
        next_states = set()
        for state in current:
            try:
                next_states.update(fa.get_transitions(state, sym))
            except AttributeError:
                next_states.update(fa.get('transitions', {}).get(state, {}).get(sym, set()))
        if not next_states:
            return False
        current = next_states

    try:
        return any(state in fa.final_states for state in current)
    except AttributeError:
        return any(state in fa.get('final_states', set()) for state in current)