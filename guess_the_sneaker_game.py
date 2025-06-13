import tkinter as tk
import random

# List of (emoji, sneaker_name)
SNEAKERS = [
    ("👟", "Nike Air Max"),
    ("🥾", "Timberland Boot"),
    ("🥿", "Flat Shoe"),
    ("👠", "High Heel"),
    ("👡", "Sandal"),
    ("👢", "Boot"),
]

def new_round():
    global current
    current = random.choice(SNEAKERS)
    emoji_label.config(text=current[0])
    guess_var.set("")
    result_label.config(text="")

def check_guess():
    guess = guess_var.get()
    if current is not None and guess == current[1]:
        result_label.config(text="Correct! 🎉", fg="green")
    elif current is not None:
        result_label.config(text=f"Wrong! It was: {current[1]}", fg="red")
    else:
        result_label.config(text="No sneaker selected.", fg="orange")

root = tk.Tk()
root.title("Guess the Sneaker")

emoji_label = tk.Label(root, text="", font=("Arial", 100))
emoji_label.pack(pady=10)

guess_var = tk.StringVar()
options = [name for _, name in SNEAKERS]
guess_menu = tk.OptionMenu(root, guess_var, *options)
guess_menu.pack(pady=5)

guess_btn = tk.Button(root, text="Guess", command=check_guess)
guess_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

next_btn = tk.Button(root, text="Next Sneaker", command=new_round)
next_btn.pack(pady=5)

# Start the first round
current = None
new_round()

root.mainloop()