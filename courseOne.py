
# Variables and basic data types
income = 5000  # Integer
expenses = 3000.50  # Float
description = "Monthly Budget"  # String
is_profitable = income > expenses  # Boolean

print(f"Income: ${income}")
print(f"Expenses: ${expenses}")
print(f"Is the budget profitable? {is_profitable}")


# Lists and Tuples
# List of expenses
expenses_list = [1000, 500, 200, 300]  # List
# Tuple of fixed expenses
fixed_expenses = (1000, 200)  # Tuple
# Adding a new expense to the list  

expenses_list.append(150)  # Adding a new expense
# Removing an expense from the list
expenses_list.remove(200)  # Removing an expense
# Accessing elements in the list and tuple
print(f"Updated expenses list: {expenses_list}")
print(f"Fixed expenses: {fixed_expenses}")
# Slicing the list 
print(f"First two expenses: {expenses_list[:2]}")
print(f"Last expense: {expenses_list[-1]}")
# Dictionary and Sets
# Dictionary of monthly expenses
monthly_expenses = {
    "Rent": 1200,
    "Utilities": 300,
    "Groceries": 400,
    "Transportation": 150
}
# Adding a new expense to the dictionary
monthly_expenses["Entertainment"] = 200  # Adding a new expense
# Removing an expense from the dictionary
monthly_expenses.pop("Transportation")  # Removing an expense
# Accessing elements in the dictionary
print(f"Monthly expenses: {monthly_expenses}")
# Set of unique expenses
unique_expenses = {1200, 300, 400, 150, 200}  # Set
# Adding a new unique expense to the set
unique_expenses.add(250)  # Adding a new unique expense
# Removing a unique expense from the set
unique_expenses.remove(150)  # Removing a unique expense
# Accessing elements in the set
print(f"Unique expenses: {unique_expenses}")
# Control flow statements
# If-else statement to check if the budget is profitable
if is_profitable:
    print("The budget is profitable.")
else:
    print("The budget is not profitable.")
# For loop to iterate through the list of expenses    
for expense in expenses_list:
    print(f"Expense: ${expense}")
# While loop to calculate total expenses  
total_expenses = 0
while expenses_list:
    total_expenses += expenses_list.pop(0)  # Removing the first expense
print(f"Total expenses: ${total_expenses}")
# Functions to calculate profit and loss
def calculate_profit(income, expenses):
    """Calculate profit or loss."""
    return income - expenses  # Function to calculate profit or loss  

