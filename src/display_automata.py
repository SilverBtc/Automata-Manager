# Display automaton details
def display_automaton(fa):
    print("\nFinite Automaton Details:")
    print(f"Alphabet: {sorted(fa.alphabet)}")
    print(f"States: {sorted(fa.states)}")
    print(f"Initial states: {sorted(fa.initial_states)}")
    print(f"Final states: {sorted(fa.final_states)}")
    print("\nTransition Table:")
    symbols = sorted(fa.alphabet)
    # Calculate the width for the state column and symbol columns
    state_col_width = 12
    symbol_col_width = 5
    
    # Create header with proper spacing
    header = "   State   ".ljust(state_col_width) + "| " + " | ".join(s.center(symbol_col_width) for s in symbols)
    print(header)
    print('-' * len(header))
    
    for state in sorted(fa.states):
        # Format state representation
        state_str = []
        if state in fa.initial_states:
            state_str.append("->")
        if state in fa.final_states:
            state_str.append('<-')
        if not (state in fa.initial_states or state in fa.final_states):
            state_str.append("  ")
        state_str.append(" " + str(state))
        state_str = ''.join(state_str).ljust(state_col_width)
        
        # Format transitions for each symbol
        transitions = []
        for symbol in symbols:
            targets = fa.get_transitions(state, symbol)
            if targets:
                transitions.append(','.join(map(str, sorted(targets))).center(symbol_col_width))
            else:
                transitions.append('-'.center(symbol_col_width))
        
        # Print the row
        print(state_str + "| " + " | ".join(transitions))
