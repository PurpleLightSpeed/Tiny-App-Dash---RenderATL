import tkinter as tk
import random

# set the dimensions of the window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

def move_sneaker():
    x = random.radiant(0, WINDOW_WIDTH - 100)
    y = random.radiant(0, WINDOW_HEIGHT - 100)
    sneaker_button.place(x=x, y=y)

def sneaker_clicked():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    move_sneaker()

# Initialize the main application window
root = tk.Tk()
root.title("Click the Sneaker Game")