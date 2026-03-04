import tkinter as tk
from logic import generate_password

def generate():
    try:
        length = int(length_entry.get())
        pwd = generate_password(
            length,
            numbers_var.get(),
            symbols_var.get()
        )
        result.set(pwd)

    except Exception as e:
        result.set(str(e))


root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length").pack()

length_entry = tk.Entry(root)
length_entry.pack()

numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()