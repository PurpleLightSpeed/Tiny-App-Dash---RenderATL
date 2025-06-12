import tkinter as tk
from datetime import datetime, timedelta

#Seting the target date for the countdown
TARGET_DATE = datetime(2025, 7, 12, 0, 0, 0)

def update_countdown():
    now = datetime.now()
    remaining = TARGET_DATE - now

    if remaining.total_seconds() > 0:
        days = remaining.days
        hours, rem = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        countdown_text = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds remaining until the event!"
    else:
        countdown_text = "The event has arrived!"
        
    countdown_label.config(text=countdown_text)
    root.after(1000, update_countdown)  # Update every second

root = tk.Tk()
root.title("Countdown to July 12, 2025")

countdown_label = tk.Label(root, text="", font=("Arial", 18), wraplength=400)
countdown_label.pack(pady=40)

update_countdown()

root.mainloop()