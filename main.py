# Virtual Environment: Module
from collections import defaultdict

# Finite Automata Module
from FiniteAutomata import FiniteAutomata
from src.read_automata import read_automaton
from src.display_automata import display_automaton
from src.is_deterministic import is_deterministic
from src.is_complete import is_complete
from src.is_standard import is_standard
from src.standardize import standardize
from src.determinize import determinize
from src.minimize import minimize
from src.complete import complete
from src.recognize_word import recognize_word
from src.determinize_and_complete import determinize_and_complete
from src.graphic import AutomataGUI

if __name__ == "__main__":
    app = AutomataGUI()
    app.mainloop()

