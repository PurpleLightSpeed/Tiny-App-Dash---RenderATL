import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# List of (image_path, sneaker_name)
SNEAKERS = [
    ("airmax.jpg", "Nike Air Max"),
    ("jordan1.jpg", "Air Jordan 1"),
    ("blazer.jpg", "Nike Blazer"),
    # Add more (image_path, name) pairs as needed
]

def crop_image(path):
    img = Image.open(path)
    w, h = img.size
    # Crop to show only the middle part (adjust as needed)
    left = w // 4
    top = h // 4
    right = left + w // 2
    bottom = top + h // 2
    cropped = img.crop((left, top, right, bottom))
    return ImageTk.PhotoImage(cropped.resize((200, 200)))

def new_round():
    global current, img_tk
    current = random.choice(SNEAKERS)
    img_tk = crop_image(current[0])
    img_label.config(image=img_tk)
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

img_label = tk.Label(root)
img_label.pack(pady=10)

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
img_tk = None
new_round()

root.mainloop()