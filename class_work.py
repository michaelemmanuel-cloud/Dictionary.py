import tkinter as tk
from tkinter import ttk

def search_word():
    word = entry.get().lower()
    if word:
        result_label.config(text=f"Searching for: {word}")
    else:
        result_label.config(text="Word not found")

root = tk.Tk()
root.title("Dictionary Search")

entry = ttk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

search_button = ttk.Button(root, text="Search", command=search_word)
search_button.grid(row=0, column=1, padx=10, pady=10)

result_label = ttk.Label(root, text="", wraplength=300)
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
