# A GUI application that displays a random Nike slogan when a button is clicked.
import tkinter as tk
import random

# Dictionary of Nike slogans
slogans = [ 
    "Just Do It",
    "There Is No Finish Line",
    "Believe in Something",
    "Find Your Greatness",
    "Make Yourself Better",
    "Dream Crazy",
    "Unleash the Athlete in You",
]

# Function to display a random slogan
def show_slogan():
    # Select a random slogan from the list and update the label
    slogan_label.config(text=random.choice(slogans))

# Create the main application window
root = tk.Tk()
root.title("Nike Slogan Picker")

# Set the size of the window
slogan_label = tk.Label(root, text="Click the button foa a Nike slogan!",font=("Arial", 14), wraplength=300)
# Pack the label into the window
slogan_label.pack(pady=20)

# Create a button that will trigger the slogan display
slogan_button = tk.Button(root, text="Show Slogan", command=show_slogan, font=("Arial", 12))
# Pack the button into the window
slogan_button.pack(pady=10)

root.mainloop()
# Start the main event loop
# This keeps the window open and responsive
# until the user closes it
# End of the application