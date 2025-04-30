import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_text = text_box.get("1.0", tk.END).strip()
    if user_text:
        messagebox.showinfo("Text Content", f"You entered: {user_text}")
    else:
        messagebox.showwarning("Empty Text", "Please enter some text!")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Simple Tkinter App")

    # Create a Text widget
    text_box = tk.Text(root, height=10, width=40)
    text_box.pack(pady=10)

    # Create a Button widget
    submit_button = tk.Button(root, text="Submit", command=on_button_click)
    submit_button.pack(pady=5)

    # Run the application
    root.mainloop()