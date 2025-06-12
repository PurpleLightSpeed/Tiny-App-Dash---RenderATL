#
import tkinter as tk
import random

slogans = [ 
    "Just Do It",
    "There Is No Finish Line",
    "Believe in Something",
    "Find Your Greatness",
    "Make Yourself Better",
    "Dream Crazy",
    "Unleash the Athlete in You",
]

def show_slogan():
    slogan_label.config(text=random.choice(slogans))

root = tk.Tk()
root.title("Nike Slogan Picker")

slogan_label = tk.Label(root, text="Click the button foa a Nike slogan!",font=("Arial", 14), wraplength=300)
slogan_label.pack(pady=20)

slogan_button = tk.Button(root, text="Show Slogan", command=show_slogan, font=("Arial", 12))
slogan_button.pack(pady=10)

root.mainloop()