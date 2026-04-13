todo_list = []

print("\nTo-Do List Manager!")
print("\nPress 1 to Add Task.")
print("Press 2 to View Task.")
print("Press 3 to Remove task.")
print("Press 4 to Exit.\n")

while True:

    choice = input("Enter your choice: ").strip()

    # ADD
    if choice == "1":
        while True:
            task = input("Enter task (type 'exit' to stop adding): ").strip()

            if task.lower() == "exit":
                break
            elif task:
                todo_list.append(task)
                print("Task added!")
            else:
                print("Task cannot be empty.")

    # VIEW
    elif choice == "2":
        if not todo_list:
            print("Your list is empty.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")

    # REMOVE
    elif choice == "3":
        if not todo_list:
            print("Nothing to remove.")
        else:
            while True:
                print("\nYour Tasks:")
                for idx, task in enumerate(todo_list, start=1):
                    print(f"{idx}. {task}")

                remove = input("Enter task number to remove (or 'exit'): ")

                if remove.lower() == "exit":
                    break

                if not todo_list:
                    break

                if remove.isdigit():
                    index = int(remove) - 1

                    if 0 <= index < len(todo_list):
                        removed = todo_list.pop(index)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid number.")
                else:
                    print("Enter a valid number.")

    # EXIT
    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")




