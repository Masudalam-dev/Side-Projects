# Add Expense

print("Welcome to Expense Tracker Website. Add your today Expenses.")
print("Enter 1 👉 add expenses. 2 👉 show expense. 3 👉 See total expenses.")
print("---------------------------------------------------------------\n")

expenses = []

while True:
    choice = input("Enter number: ").strip()
    categories = ["Food", "Travel", "Shopping", "Entra"]
    # Add Expenses
    if choice == "1":
        for cat in categories:
            while True:
                amount = input(f"Enter Your {cat} Expenses in $: ").strip()
                if amount.isdigit():
                    expenses.append(amount)
                    break
                else:
                    print("Invalid Input. Please enter amount in digit.")

    # Show the Expenses.
    elif choice == "2":
        if not expenses:
            print("Your list is Empty:")
        else:
            print("Your Expenses by Category.")
            for idx, individual_category in enumerate(categories and expenses, start=1):
                print(f"{idx}.{individual_category}: ")

            print(expenses)

    elif choice == "4":
        break
    else:
        print("Invalid Input!")
        break






