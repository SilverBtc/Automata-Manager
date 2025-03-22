from FiniteAutomata import FiniteAutomata

# Read automata from file
def read_automaton(filename):
    # Read lines from file
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    num_symbols = int(lines[0])
    alphabet = set(chr(ord('a') + i) for i in range(num_symbols))

    num_states = int(lines[1])
    states = set(range(num_states))

    initial_parts = list(map(int, lines[2].split()))
    initial_count = initial_parts[0]
    initial_states = set(initial_parts[1:1+initial_count])

    final_parts = list(map(int, lines[3].split()))
    final_count = final_parts[0]
    final_states = set(final_parts[1:1+final_count])

    num_transitions = int(lines[4])
    transition_lines = lines[5:5+num_transitions]

    fa = FiniteAutomata()
    fa.states = states
    fa.alphabet = alphabet
    fa.initial_states = initial_states
    fa.final_states = final_states

    # Parse transition lines
    for line in transition_lines:
        i = 0
        while i < len(line) and line[i].isdigit():
            i += 1
        if i == 0 or i >= len(line):
            raise ValueError(f"Invalid transition line: {line}")
        source = int(line[:i])
        symbol = line[i]
        target = int(line[i+1:])
        fa.add_transition(source, symbol, target)

    return fa