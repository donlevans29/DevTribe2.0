import tkinter as tk

def calculate_profit():
    income = float(income_entry.get())
    expenses = float(expenses_entry.get())
    profit = income - expenses
    result_label.config(text=f"Cashflow: ${profit:.2f}")

# Create the main window
root = tk.Tk()
root.title("Budget Calculator")

# Create input fields
tk.Label(root, text="Income:").grid(row=0, column=0)
income_entry = tk.Entry(root)
income_entry.grid(row=0, column=1)

tk.Label(root, text="Expenses:").grid(row=1, column=0)
expenses_entry = tk.Entry(root)
expenses_entry.grid(row=1, column=1)

# Create a button to calculate profit
calculate_button = tk.Button(root, text="Calculate Profit", command=calculate_profit)
calculate_button.grid(row=2, column=0, columnspan=2)

# Label to display the result
result_label = tk.Label(root, text="Profit: $0.00")
result_label.grid(row=3, column=0, columnspan=2)

# Run the application
root.mainloop()