import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

operation_var = tk.StringVar(root)
operation_var.set('+')  # Default value
tk.Label(root, text="Choose operation:").grid(row=2, column=0, padx=10, pady=10)
tk.OptionMenu(root, operation_var, '+', '-', '*', '/').grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
