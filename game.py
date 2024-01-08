import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Number Guessing Game")

        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 10  # Set a maximum number of attempts
        self.history = []

        self.mode_var = tk.StringVar()
        self.mode_var.set("Any")  # Default mode is guessing any number

        self.label_mode = tk.Label(self.window, text="Select Mode:")
        self.label_mode.pack()

        self.radio_any = tk.Radiobutton(self.window, text="Any Number", variable=self.mode_var, value="Any")
        self.radio_any.pack()

        self.radio_odd = tk.Radiobutton(self.window, text="Odd Number", variable=self.mode_var, value="Odd")
        self.radio_odd.pack()

        self.radio_even = tk.Radiobutton(self.window, text="Even Number", variable=self.mode_var, value="Even")
        self.radio_even.pack()

        self.label = tk.Label(self.window, text="Guess the number:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.window)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack(pady=10)

        self.play_again_button = tk.Button(self.window, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)
        self.play_again_button.pack_forget()

        self.initialize_game()

        self.window.mainloop()

    def initialize_game(self):
        # Generate a random number based on the selected mode
        if self.mode_var.get() == "Odd":
            self.secret_number = random.randint(1, 50) * 2 - 1  # Ensures the number is odd and between 1 and 100
        elif self.mode_var.get() == "Even":
            self.secret_number = random.randint(1, 50) * 2  # Ensures the number is even and between 1 and 100
        else:
            self.secret_number = random.randint(1, 100)

    def check_guess(self):
        try:
            guess = int(self.entry.get())

            if guess <= 0 or guess > 100:
                messagebox.showerror("Invalid Input", "Please enter a positive integer between 1 and 100.")
                return

            self.attempts += 1

            if self.mode_var.get() == "Odd" and guess % 2 == 0:
                self.result_label.config(text="Incorrect Guess. You selected Odd mode. Enter an odd number.")
            elif self.mode_var.get() == "Even" and guess % 2 != 0:
                self.result_label.config(text="Incorrect Guess. You selected Even mode. Enter an even number.")
            else:
                if guess == self.secret_number:
                    self.result_label.config(text=f"Congratulations! You guessed the correct number in {self.attempts} attempts.")
                    self.guess_button.config(state=tk.DISABLED)
                    self.play_again_button.pack(pady=10)
                elif guess < self.secret_number:
                    self.result_label.config(text="Incorrect Guess. Too low. Try again.")
                else:
                    self.result_label.config(text="Incorrect Guess. Too high. Try again.")

                self.history.append(guess)

                if self.attempts == self.max_attempts:
                    self.result_label.config(text=f"Sorry, you've reached the maximum attempts. The correct number was {self.secret_number}.")
                    self.guess_button.config(state=tk.DISABLED)
                    self.play_again_button.pack(pady=10)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive integer.")

    def reset_game(self):
        self.attempts = 0
        self.history = []
        self.guess_button.config(state=tk.NORMAL)
        self.play_again_button.pack_forget()
        self.result_label.config(text="Guess the number:")
        self.entry.delete(0, tk.END)
        self.initialize_game()

if __name__ == "__main__":
    NumberGuessingGame()
