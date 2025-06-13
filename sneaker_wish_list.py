import tkinter as tk

def add_sneaker():
    sneaker = entry.get().strip()
    if sneaker:
        listbox.insert(tk.END, sneaker)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Sneaker Wish List")

tk.Label(root, text="Enter Sneaker Name:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

add_btn = tk.Button(root, text="Add to Wish List", command=add_sneaker)
add_btn.pack(pady=5)

tk.Label(root, text="Your Wish List:").pack(pady=5)
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=5)

root.mainloop()