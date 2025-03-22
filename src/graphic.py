import customtkinter as ctk
import time
from tkinter import messagebox
from PIL import Image, ImageTk
from src.read_automata import read_automaton
from src.is_deterministic import is_deterministic
from src.is_complete import is_complete
from src.is_standard import is_standard
from src.standardize import standardize
from src.determinize import determinize
from src.minimize import minimize
from src.complete import complete
from src.recognize_word import recognize_word
from src.determinize_and_complete import determinize_and_complete

# Initialize GUI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AutomataGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Automata Manager")
        self.geometry("900x600")
        self.current_fa = None

        # Load and display background image
        self.background_image = ImageTk.PhotoImage(Image.open("assets/background.png"))
        self.background_label = ctk.CTkLabel(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Load and display logo (maintaining aspect ratio)
        self.logo = Image.open("assets/LOGO.png")
        self.logo = self.logo.resize((250, 120), Image.ANTIALIAS)  # Resize while maintaining aspect ratio
        self.logo_image = ImageTk.PhotoImage(self.logo)
        self.logo_label = ctk.CTkLabel(self, image=self.logo_image, text="")
        self.logo_label.pack(pady=20)

        # Main menu setup
        self.setup_main_menu()

    def setup_main_menu(self):
        self.label = ctk.CTkLabel(self, text="Load an automaton (1-44) or Exit:", font=("Arial", 18))
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter number", width=200)
        self.entry.pack(pady=5)

        self.load_button = ctk.CTkButton(self, text="Load", command=self.load_automaton, width=150)
        self.load_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red", width=150)
        self.exit_button.pack(pady=10)

    def load_automaton(self):
        automaton_number = self.entry.get()
        if not automaton_number.isdigit() or not (1 <= int(automaton_number) <= 44):
            messagebox.showerror("Error", "Invalid automaton number!")
            return

        # Display loading bar
        self.label.configure(text="Loading...")
        progress = ctk.CTkProgressBar(self)
        progress.pack(pady=10)
        progress.set(0)
        self.update()

        for i in range(100):
            time.sleep(0.01)
            progress.set(i / 100)
            self.update()

        # Load automaton file
        try:
            self.current_fa = read_automaton(f"data/fa_{automaton_number}.txt")
            messagebox.showinfo("Success", f"Automaton {automaton_number} loaded successfully!")
            self.display_functions()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load automaton: {e}")

    def display_functions(self):
        self.label.configure(text="Choose a function:")
        self.clear_menu_buttons()

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=20, padx=20, fill='both', expand=True)

        functions = {
            "Display": self.display_automaton_table,
            "Is Deterministic": is_deterministic,
            "Is Complete": is_complete,
            "Is Standard": is_standard,
            "Standardize": standardize,
            "Determinize": determinize,
            "Minimize": lambda fa: minimize or "Minimized Successfully",
            "Complete": complete,
            "Recognize Word": recognize_word,
            "Determinize & Complete": determinize_and_complete,
        }

        for name, func in functions.items():
            ctk.CTkButton(button_frame, text=name, command=lambda f=func: self.execute_function(f), width=250).pack(pady=5)

        self.exit_button_2 = ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red", width=150)
        self.exit_button_2.pack(pady=20)

    def clear_menu_buttons(self):
        for widget in self.winfo_children():
            widget.pack_forget()

    def execute_function(self, func):
        if self.current_fa is None:
            messagebox.showerror("Error", "No automaton loaded!")
            return

        try:
            if func == self.display_automaton_table:
                func(self.current_fa)
            else:
                result = func(self.current_fa)
                self.display_result(func.__name__, str(result))  # Ensure output is string formatted
        except Exception as e:
            messagebox.showerror("Error", f"Function execution failed: {e}")
    def display_result(self, function_name, result):
        self.clear_menu_buttons()
        self.label = ctk.CTkLabel(self, text=f"{function_name} Result:", font=("Arial", 18))
        self.label.pack(pady=20)

        result_text = ctk.CTkTextbox(self, height=300, width=600)
        result_text.insert("1.0", result)  # Directly inserting the output
        result_text.configure(state="disabled")
        result_text.pack(pady=10)

        ctk.CTkButton(self, text="Back to Menu", command=self.display_functions, width=200).pack(pady=10)
        ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red", width=200).pack(pady=10)

    def display_automaton_table(self, fa):
        self.clear_menu_buttons()
        self.label = ctk.CTkLabel(self, text="Automaton Details:", font=("Arial", 18))
        self.label.pack(pady=20)

        # Display automaton details
        details = [
            f"Number of symbols: {len(fa.alphabet)}",
            f"Alphabet: A = {{{', '.join(map(str, sorted(fa.alphabet)))}}}",
            f"Number of states: {len(fa.states)}",
            f"Initial state: {', '.join(map(str, sorted(fa.initial_states)))}",
            f"Final states: {', '.join(map(str, sorted(fa.final_states)))}",
            f"Number of transitions: {sum(len(targets) for state in fa.states for targets in fa.transitions[state].values())}"
        ]

        for detail in details:
            ctk.CTkLabel(self, text=detail).pack(pady=5)

        # Display transitions
        transition_label = ctk.CTkLabel(self, text="Transitions:", font=("Arial", 18))
        transition_label.pack(pady=10)

        for state in sorted(fa.states):
            for symbol in sorted(fa.alphabet):
                next_states = fa.get_transitions(state, symbol)
                for next_state in sorted(next_states):
                    transition_text = f"{state} -> {symbol} -> {next_state}"
                    ctk.CTkLabel(self, text=transition_text).pack(pady=2)

        ctk.CTkButton(self, text="Back to Menu", command=self.display_functions, width=200).pack(pady=10)
        ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red", width=200).pack(pady=10)

if __name__ == "__main__":
    app = AutomataGUI()
    app.mainloop()
