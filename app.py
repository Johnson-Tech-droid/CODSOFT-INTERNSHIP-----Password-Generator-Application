import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special 
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
            
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
            
    return pwd

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError("Password length must be positive.")
        include_numbers = var_numbers.get()
        include_special = var_special.get()
        password = generate_password(length, include_numbers, include_special)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

var_numbers = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).grid(row=1, column=0, padx=10, pady=5, sticky="w")

var_special = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).grid(row=2, column=0, padx=10, pady=5, sticky="w")

tk.Label(root, text="Generated Password:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_password = tk.Entry(root, state="normal", width=30)
entry_password.grid(row=3, column=1, padx=10, pady=10)

btn_generate = tk.Button(root, text="Generate Password", command=on_generate)
btn_generate.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
