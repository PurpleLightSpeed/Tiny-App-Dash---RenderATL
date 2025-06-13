import tkinter as tk
import random
#functools is a module that provides higher-order functions that act on or return other functions.
#partial is a function that allows you to fix a certain number of arguments of a function and generate a new function.
from functools import partial

root = tk.Tk()
root.title("Shoe Memory Game")

# Sneaker emojis as placeholders for images
SNEAKERS = ["👟", "🥾", "🥿", "👠", "👡", "👢"]
PAIRS = SNEAKERS * 2
random.shuffle(PAIRS)

buttons = []
flipped = []
matched = []

def check_match():
    if len(flipped) == 2:
        idx1, idx2 = flipped
        if PAIRS[idx1] == PAIRS[idx2]:
            matched.extend(flipped)
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

for i in range(4):
    for j in range(3):
        idx = i * 3 + j
        btn = tk.Button(root, text="❓", font=("Arial", 32), width=4, height=2,
                        command=partial(on_click, idx))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(btn)

root.mainloop()