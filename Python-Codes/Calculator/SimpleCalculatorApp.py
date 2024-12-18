import tkinter as tk
from tkinter import messagebox

# Function to perform the selected operation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Please select an operation.")
            return

        # Display result
        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Labels and entry fields
tk.Label(root, text="Enter First Number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Second Number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Dropdown menu for operations
tk.Label(root, text="Select Operation:").grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation
operations_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operations_menu.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
calculate_btn = tk.Button(root, text="Calculate", command=calculate)
calculate_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the GUI event loop
root.mainloop()
