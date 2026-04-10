
to_to_list = []
print("------- To-D0 List Creator -------")
print("Add your task one by one: Type 'exit' to finish.\n")
while True:
    user_data = input("Enter your To-Do List: ").strip().lower()  # .strip will remove the accidental space of both the side
    if user_data.lower() == "exit":
        break
    else:
        to_to_list.append(user_data)

print("\n------- Your Final To-Do List -------")
if not to_to_list:
    print("Your list is empty!")
else:
    idx = 0
    for data in to_to_list:
        idx += 1
        print(f"{idx}. {data}")

