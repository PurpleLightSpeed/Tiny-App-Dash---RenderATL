import tkinter as tk
import random

#List of Nike Sneakers
sneaker = [
    "Nike Air Max",
    "Nike Air Force 1",
    "Nike Dunk Low",
    "Nike Blazer Mid",
    "Nike React Infinity Run",
    "Nike ZoomX Vaporfly",
    "Nike Pegasus Trail 3",
    "Nike Air Zoom Tempo",
    "Nike Air Jordan 1 Retro High OG",
    "Nike Air Presto React"
]

def show_sneaker():
    # Select a random sneaker from the list and update the label
    sneaker_label.config(text=random.choice(sneaker))

# Create the main application window
root = tk.Tk()
root.title("Nike Sneaker Picker")

# Set the size of the window
sneaker_label = tk.Label(root, text="Click the button for a Nike sneaker!", font=("Arial", 14), wraplength=300)
# Pack the label into the window
sneaker_label.pack(pady=20)
# Create a button that will trigger the sneaker display
sneaker_button = tk.Button(root, text="Show Sneaker", command=show_sneaker, font=("Arial", 12))
# Pack the button into the window
sneaker_button.pack(pady=10)
# Start the main event loop
root.mainloop()
# This keeps the window open and responsive