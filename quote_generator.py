# Random Quote Generator - Python GUI Project

import tkinter as tk
import random
from tkinter import messagebox

# Quotes dictionary by category
quotes = {
    "Motivational": [
        "Do what you can, with what you have, where you are. 💪",
        "Dream big and dare to fail. 💫",
        "Stay positive, work hard, make it happen! 🌟",
        "You are stronger than you think. 💖"
    ],
    "Funny": [
        "Life is short, smile while you still have teeth! 😄",
        "Hustle in silence and let success make the noise! 🚀",
        "Life is better when you laugh. 😆",
        "I am on energy saving mode. 😎"
    ],
    "Love": [
        "Love is not about how many days, months or years you’ve been together. ❤️",
        "You are my today and all of my tomorrows. 💞",
        "In a sea of people, my eyes will always search for you. 🌹",
        "Every love story is beautiful, but ours is my favorite. 💖"
    ]
}

# Function to show random quote from selected category
def generate_quote(category):
    quote = random.choice(quotes[category])
    quote_label.config(text=quote)

# Function to copy current quote to clipboard
def copy_quote():
    current_quote = quote_label.cget("text")
    if current_quote:
        root.clipboard_clear()
        root.clipboard_append(current_quote)
        messagebox.showinfo("Copied", "Quote copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No quote to copy!")

# GUI setup
root = tk.Tk()
root.title("Random Quote Generator - Categories")
root.geometry("550x350")
root.configure(bg="#f0f8ff")  # light background

# Title label
tk.Label(root, text="✨ Random Quote Generator ✨", font=("Helvetica", 16, "bold"), bg="#f0f8ff").pack(pady=10)

# Quote display label
quote_label = tk.Label(root, text="", wraplength=500, justify="center", font=("Helvetica", 12), bg="#f0f8ff")
quote_label.pack(pady=30)

# Frame for category buttons
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

tk.Button(frame, text="Motivational", command=lambda: generate_quote("Motivational"), bg="#90ee90", width=15).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Funny", command=lambda: generate_quote("Funny"), bg="#ffb6c1", width=15).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Love", command=lambda: generate_quote("Love"), bg="#add8e6", width=15).grid(row=0, column=2, padx=5)

# Copy button
tk.Button(root, text="Copy Quote", command=copy_quote, bg="#ffe4b5", width=20).pack(pady=10)

# Start GUI loop
root.mainloop()
