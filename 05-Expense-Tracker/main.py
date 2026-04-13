# Add Expense
from unicodedata import category

print("Welcome to Expense Tracker Website. Add your today Expenses.")
print("Enter 1 👉 add expenses. 2 👉 show expense. 3 👉 See total expenses.")
print("---------------------------------------------------------------\n")

choice = input("Enter number: ")
expenses = []

# Add Expenses
if choice == "1":
    categories = ["Food", "Travel", "Shopping", "Entra"]
    for cat in categories:
        while True:
            amount = input(f"Enter Your {cat} Expenses in $: ")
            if amount.isdigit():
                expenses.append(amount)
                break
            else:
                print("Invalid Input. Please enter amount in digit.")

else:
    print("Invalid Input!")

print(expenses)
# Show Expenses in list with numbering




