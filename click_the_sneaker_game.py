import tkinter as tk
import random

# set the dimensions of the window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

# Function to move the sneaker button to a random position
def move_sneaker():
    x = random.randint(0, WINDOW_WIDTH - 100)
    y = random.randint(0, WINDOW_HEIGHT - 100)
    sneaker_button.place(x=x, y=y)

# Function to handle sneaker button click
def sneaker_clicked():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    move_sneaker()

# Initialize the main application window
root = tk.Tk()
root.title("Click the Sneaker Game")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Create a label to display the score
score = 0
score_label = tk.Label(root, text = "score: 0", font = ("Arial", 16))
score_label.pack(pady=10)

# Create a button that represents the sneaker
sneaker_button = tk.Button(root, text="👟", font=("Arial", 50), command=sneaker_clicked, bd = 0)
move_sneaker()  # Position the sneaker button randomly

root.mainloop()  # Start the main event loop
