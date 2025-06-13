import tkinter as tk
import random
from functools import partial

root = tk.Tk()
root.title("Shoe Memory Game")

SNEAKERS = ["👟", "🥾", "🥿", "👠", "👡", "👢"]

def reset_game():
    global PAIRS, buttons, flipped, matched
    PAIRS = SNEAKERS * 2
    random.shuffle(PAIRS)
    flipped.clear()
    matched.clear()
    for btn in buttons:
        btn.config(text="❓", state="normal")
    win_label.config(text="")

def check_match():
    if len(flipped) == 2:
        idx1, idx2 = flipped
        if PAIRS[idx1] == PAIRS[idx2]:
            matched.extend(flipped)
            if len(matched) == len(PAIRS):
                win_label.config(text="You win! 🎉")
                for btn in buttons:
                    btn.config(state="disabled")
        else:
            buttons[idx1].config(text="❓")
            buttons[idx2].config(text="❓")
        flipped.clear()

def on_click(idx):
    if idx in matched or idx in flipped:
        return
    buttons[idx].config(text=PAIRS[idx])
    flipped.append(idx)
    root.after(500, check_match)

buttons = []
flipped = []
matched = []

# Win message label
win_label = tk.Label(root, text="", font=("Arial", 20), fg="green")
win_label.pack(pady=10)

# Reset button
reset_btn = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_btn.pack(pady=5)

# Game grid
frame = tk.Frame(root)
frame.pack()

for i in range(4):
    for j in range(3):
        idx = i * 3 + j
        btn = tk.Button(frame, text="❓", font=("Arial", 32), width=4, height=2,
                        command=partial(on_click, idx))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(btn)

reset_game()  # Initialize the game

root.mainloop()