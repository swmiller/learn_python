import tkinter as tk

root = tk.Tk()


def miles_to_km(miles):
    """
    Convert miles to kilometers.

    Args:
        miles (float): The distance in miles.

    Returns:
        float: The distance in kilometers.
    """
    return miles * 1.60934


def create_ui():
    root.title("Mile to Km Converter")
    root.geometry("320x140")
    root.resizable(False, False)

    # Row 0: Miles label and entry
    miles_label = tk.Label(root, text="Miles:")
    miles_label.grid(row=0, column=0, padx=10, pady=15, sticky="e")
    miles_var = tk.StringVar()
    miles_entry = tk.Entry(root, textvariable=miles_var, width=12)
    miles_entry.grid(row=0, column=1, padx=10, pady=15, sticky="w")

    # Row 1: Result label
    result_var = tk.StringVar(value="is equal to 0 kilometers.")
    result_label = tk.Label(root, textvariable=result_var, anchor="w", width=28)
    result_label.grid(row=1, column=0, columnspan=2, pady=5, padx=(10, 0), sticky="w")

    def set_result(n):
        result_var.set(f"is equal to {n} kilometers.")

    def on_calculate():
        miles_str = miles_var.get().strip()
        if not miles_str.isdigit():
            set_result("Invalid input")
            return
        miles = int(miles_str)
        km = miles_to_km(miles)
        set_result(f"{km:.3f}")

    # Row 2: Calculate button
    calc_btn = tk.Button(root, text="Calculate", command=on_calculate, width=15)
    calc_btn.grid(row=2, column=0, columnspan=2, pady=15)


def main():
    create_ui()
    root.mainloop()


if __name__ == "__main__":
    main()
