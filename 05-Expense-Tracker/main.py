
print("Welcome to Expense Tracker Website. Add your today Expenses.")
print("Enter 1 👉 add expenses. 2 👉 show expense. 3 👉 See total expenses. 4 👉 to Exit.")
print("---------------------------------------------------------------\n")

expenses = []

while True:
    while True:
        choice = input("Enter number: ").strip()
        is_digit = choice.isdigit()

        if is_digit:
            if 0 < int(choice) <= 4:
                break
            else:
                print("Please Enter Number between 1 to 4")
        else:
            print("Invalid Input! You have not entered a number.")


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
            idx = 0
            for cat,amt in zip(categories,expenses):
                idx += 1
                print(f"{idx}.{cat} = ${amt}")

    # Show the total Spending
    elif choice == "3":
        if not expenses:
            print("Your Spending is 0.")
        else:
            total = sum(map(int,expenses))
            print(f"Your total Expending: ${total}")

    # Exit
    elif choice == "4":
        print("Exit: Have a Good Day!")
        break
    else:
        print("Invalid Input!")
        break





