from collections import defaultdict

# Finite Automaton class
class FiniteAutomata:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = defaultdict(lambda: defaultdict(set))
        self.initial_states = set()
        self.final_states = set()

    def add_transition(self, source, symbol, target):
        self.states.add(source)
        self.states.add(target)
        self.transitions[source][symbol].add(target)

    def get_transitions(self, source, symbol):
        return self.transitions[source].get(symbol, set())