
todo_list = []
print("------- To-D0 List Creator -------")
print("Add your task one by one: Type 'exit' to finish.\n")
while True:
    add_task = input("Enter your To-Do List: ").strip()  # .strip will remove the accidental space of both the side
    if add_task.lower() == "exit":
        break
    else:
        todo_list.append(add_task)

    # To show Task
    for idx,task in enumerate(todo_list,start=1):
        view_task = f"{idx}.{task}"
        print(view_task)

    remove_task = input("Enter Number to remove Task: ")
    if remove_task.isdigit():
        if 1 <= remove_task <= len(todo_list):
            print(todo_list.pop(remove_task - 1))

    else:
        print("Invalid input.")




