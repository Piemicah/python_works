import tkinter as tk
from tkinter import Tk, simpledialog, messagebox



def generate_activation_keys():
    n = number_entry.get()
    messagebox.showinfo("Title", n)


root = Tk()

root.geometry("600x400")

frame = tk.Frame(root).grid(row=1, pady=100)
tk.Label(frame, text="Number of keys").grid(row=1, column=0)
number_entry = tk.Entry(frame)
number_entry.grid(row=1, column=1)


btn_submit = tk.Button(
    root, text="Click me", padx=18, pady=8, command=generate_activation_keys
)

btn_submit.grid(row=2, padx=100)


root.mainloop()
