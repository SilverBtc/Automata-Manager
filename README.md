# Finite Automata Operations Project

This project is a Python program designed to perform various operations on Finite Automata (FA). It includes functionalities such as reading an FA from a file, displaying its details, checking properties (deterministic, complete, standard), standardizing the FA, determinizing and completing the FA, minimizing the FA, testing word recognition, and creating a complementary FA.

## Features

1. **Read FA from a file**: Load a finite automaton from a `.txt` file.
2. **Display FA**: Display the automaton's details, including states, alphabet, transitions, initial states, and final states.
3. **Check Properties**:
   - Check if the FA is deterministic.
   - Check if the FA is complete.
   - Check if the FA is standard.
4. **Standardize FA**: Convert the FA to a standard form if it is not already standard.
5. **Determinize and Complete FA**: Convert a non-deterministic FA to a deterministic and complete FA.
6. **Minimize FA**: Minimize a deterministic and complete FA using Hopcroft's algorithm.
7. **Word Recognition**: Test if a given word is accepted by the FA.
8. **Complementary FA**: Create an FA that recognizes the complementary language of the given FA.

## Prerequisites

- Python 3.x
- The module : Pillow, customtkinter, collections are needed.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:SilverBtc/Automata-Manager.git
   cd Automata-Manager

2. **Prepare Input Files**:

Create a `.txt` file for each FA you want to test. Follow the format described in the Input File Format section.

Example: `fa_1.txt`, `fa_2.txt`, etc.

3. **Run the Program**:

```bash
python main.py
```

4. **Follow the Menu**:

    - The program will display a menu with options to load an FA, display its details, perform operations, and test word recognition.

    - Enter the corresponding number for the operation you want to perform.

## Input File Format
The input file must follow this structure:

1. Line 1: Number of symbols in the alphabet.
2. Line 2: Number of states.
3. Line 3: Number of initial states, followed by their labels.
4. Line 4: Number of final states, followed by their labels.
5. Line 5: Number of transitions.
6. Subsequent Lines: Transitions in the format.

Example (`fa_1.txt`):
```
2
5
1 0
1 4
6
0a0
0a1
0b0
1a2
2a3
3a4
```

## Example Usage
1. Load an FA:

    - Choose option 1 and enter the FA number (e.g., 1 for fa_1.txt).

2. Display FA:

    - Choose option 2 to display the loaded FA's details.

3. Check Properties:

    - Choose options 3, 4, or 5 to check if the FA is deterministic, complete, or standard.

4. Standardize FA:

    - Choose option 6 to standardize the FA.

5. Determinize and Complete FA:

    - Choose option 7 to determinize and complete the FA.

6. Minimize FA:

    - Choose option 8 to minimize the FA.

7. Test Word Recognition:

    - Choose option 9 and enter a word to test if it is accepted by the FA.

8. Create Complementary FA:

    - Choose option 10 to create an FA that recognizes the complementary language.

9. Exit:

    - Choose option 11 to exit the program.

## Code Structure
`main.py`: The main script that runs the program and provides the user interface.

`FiniteAutomaton` class: Represents the FA and contains methods for operations like standardization, determinization, minimization, etc.

Input files: `.txt` files containing the FA definitions.

## Contributors
Brian
Abdou-Samad
Rayan
Léo
Hector

## License
This project is licensed under the MIT License. See the LICENSE file for details.