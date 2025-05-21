import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("User Form")
root.geometry("350x220")
root.resizable(False, False)

# First Name
label_first = tk.Label(root, text="First Name:")
label_first.grid(row=0, column=0, padx=15, pady=(20, 10), sticky="e")
entry_first = tk.Entry(root, width=25)
entry_first.grid(row=0, column=1, padx=15, pady=(20, 10), sticky="w")

# Last Name
label_last = tk.Label(root, text="Last Name:")
label_last.grid(row=1, column=0, padx=15, pady=10, sticky="e")
entry_last = tk.Entry(root, width=25)
entry_last.grid(row=1, column=1, padx=15, pady=10, sticky="w")

# Date of Birth
label_dob = tk.Label(root, text="Date of Birth:")
label_dob.grid(row=2, column=0, padx=15, pady=10, sticky="e")
entry_dob = tk.Entry(root, width=25)
entry_dob.grid(row=2, column=1, padx=15, pady=10, sticky="w")


# Submit button callback
def submit_form():
    first = entry_first.get().strip()
    last = entry_last.get().strip()
    dob = entry_dob.get().strip()
    msg = f"First Name: {first}\nLast Name: {last}\nDate of Birth: {dob}"
    messagebox.showinfo("Form Submission", msg)


# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_form, width=15)
submit_btn.grid(row=3, column=1, sticky="e", padx=15, pady=(15, 20))

root.mainloop()
