# Login-Registration-System Project
# Store data in dictionary
user_pass = {}

print("Welcome to the login username project.")
print("Press 1 for Register.\nPress 2 for Login.\nPress 3 for Exit.\n")

while True:

    choice = input("Enter Your choice: ")

    if not choice.isdigit():
        print("Invalid Input!")
        continue

    elif choice == "1":
        while True:
            # Registration
            user_name = input("Enter Username: ").strip()
            if not user_name:
                print("Username can't be empty.")
            elif user_name in user_pass:
                print("Username already exists.")
            elif user_name.isdigit():
                print("Username should at least one letter.")
            elif len(user_name) < 4:
                print("Username should be at least 4 character long.")

            else:
                break

        while True:
            user_password = input("Enter Password: ").strip()
            if not user_password:
                print("Password can't be empty.")
            elif not user_password.isdigit():
                print("Password should be in number only.")
            elif len(user_password) < 5:
                print("The length of Password should be at least 5")

            else:
                break

        user_pass[user_name] = user_password
        print("Registration Successful ✅.")

    # TO login
    elif choice == "2":
        check_user_name = input("Enter Your Username: ").strip()
        check_user_password = input("Enter Your Password: ").strip()

        if check_user_name in user_pass and user_pass[check_user_name] == check_user_password:
            print("Login Successful ✅.")

        elif check_user_name not in user_pass:
            print("User not found.")
        else:
            print("Incorrect Password.")


    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Please press 1,2 or 3 to move forward.")



