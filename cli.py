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





# WIP (Work In Progress)
def create_complement(fa):
    comp = FiniteAutomata()
    comp.states = fa.states.copy()
    comp.alphabet = fa.alphabet.copy()
    comp.initial_states = fa.initial_states.copy()
    comp.transitions = fa.transitions.copy()
    comp.final_states = comp.states - fa.final_states
    return comp

# display main menu
def main():
    current_fa = None
    while True:
        print("\nMain Menu:")
        print("1. Load FA from file")
        print("2. Display current FA")
        print("3. Check if FA is deterministic")
        print("4. Check if FA is complete")
        print("5. Check if FA is standard")
        print("6. Standardize FA")
        print("7. Determinize and complete FA")
        print("8. Minimize FA")
        print("9. Test word recognition")
        print("10. Create complementary FA")
        print("11. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            fa_num = input("Enter FA number: ")
            filename = f"data/fa_{fa_num}.txt"
            try:
                current_fa = read_automaton(filename)
                print("FA loaded successfully.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '2':
            if current_fa:
                display_automaton(current_fa)
            else:
                print("No FA loaded.")
        elif choice == '3':
            if current_fa:
                res, msg = is_deterministic(current_fa)
                print(msg)
            else:
                print("No FA loaded.")
        elif choice == '4':
            if current_fa:
                res, msg = is_complete(current_fa)
                print(msg)
            else:
                print("No FA loaded.")
        elif choice == '5':
            if current_fa:
                res, msg = is_standard(current_fa)
                print(msg)
            else:
                print("No FA loaded.")
        elif choice == '6':
            if current_fa:
                new_fa, msg = standardize(current_fa)
                # current_fa = new_fa
                print(msg)
                display_automaton(new_fa)
            else:
                print("No FA loaded.")
        elif choice == '7':
            if current_fa:
                derterminize = determinize_and_complete(current_fa)
                print("Determinized and completed FA:")
                display_automaton(derterminize)
            else:
                print("No FA loaded.")
        elif choice == '8':
            if current_fa:
                minimized = minimize(current_fa)
                print("Minimized FA:")
                display_automaton(minimized)
            else:
                print("No FA loaded.")
        elif choice == '9':
            if current_fa:
                word = input("Enter word (or 'end' to stop): ")
                while word != 'end':
                    if recognize_word(current_fa, word):
                        print(f"'{word}' is accepted.")
                    else:
                        print(f"'{word}' is rejected.")
                    word = input("Enter word (or 'end' to stop): ")
            else:
                print("No FA loaded.")
        elif choice == '10':
            if current_fa:
                comp = create_complement(current_fa)
                current_fa = comp
                print("Complementary FA:")
                display_automaton(current_fa)
            else:
                print("No FA loaded.")
        elif choice == '11':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()