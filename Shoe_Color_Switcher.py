import tkinter as tk

def change_color(color):
    shoe_label.config(bg=color)
root = tk.Tk()
root.title("Shoe Color Switcher")

# Placeholder for the shoe (replace with an image if you have one)
shoe_label = tk.Label(root, text="👟", font=("Arial", 100), width=8, height=4, bg="white")
shoe_label.pack(pady=20)

# Color buttons
colors = ["white", "red", "blue", "green", "black", "yellow"]
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for color in colors:
    btn = tk.Button(button_frame, text=color.capitalize(), bg=color, fg="black",
                    width=10, command=lambda c=color: change_color(c))
    btn.pack(side="left", padx=5)

root.mainloop()