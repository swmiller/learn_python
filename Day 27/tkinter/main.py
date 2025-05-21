import tkinter as tk


def some_function(a=1, b=2):
    pass


def some_function(*args):
    for n in args:
        print(n)


root = tk.Tk()
root.geometry("600x600")

# Set window properties
root.title("Tkinter GUI")
root.minsize(width=300, height=300)

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 24))
label.pack(pady=20)

some_function(1, 2, 3, 4, 5)


root.mainloop()
