def recognize_word(fa, word):
    try:
        current = fa.initial_states
    except AttributeError:
        current = fa.get('initial_states', set())
    
    # Apply epsilon closure to initial states
    current = epsilon_closure(fa, current)

    for sym in word:
        next_states = set()
        for state in current:
            try:
                next_states.update(fa.get_transitions(state, sym))
            except AttributeError:
                next_states.update(fa.get('transitions', {}).get(state, {}).get(sym, set()))
        
        # Apply epsilon closure to the new states
        next_states = epsilon_closure(fa, next_states)
        
        if not next_states:
            return False
        current = next_states

    try:
        return any(state in fa.final_states for state in current)
    except AttributeError:
        return any(state in fa.get('final_states', set()) for state in current)

def epsilon_closure(fa, states):
    """
    Compute the epsilon closure of the given states.
    Returns all states reachable from the given states using epsilon transitions.
    """
    epsilon = 'e'  # Epsilon symbol
    result = set(states)
    stack = list(states)
    
    while stack:
        state = stack.pop()
        try:
            epsilon_states = fa.get_transitions(state, epsilon)
        except AttributeError:
            epsilon_states = fa.get('transitions', {}).get(state, {}).get(epsilon, set())
        
        for eps_state in epsilon_states:
            if eps_state not in result:
                result.add(eps_state)
                stack.append(eps_state)
    
    return result