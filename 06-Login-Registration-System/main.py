# Login-Registration-System Project
# Store data in dictionary
user_pass = {"Username": [], "Password": []}
print("Welcome to the login username project.")
print("Press 1 for Register.\nPress 2 for Login.\nPress 3 for Exit.\n")

while True:

    choice = input("Enter Your choice: ")

    if not choice.isdigit():
        print("Invalid Input!")

    elif choice == "1":
        while True:
            # Registration
            store_user_name = input("Enter Your Username: ").strip()
            if not store_user_name:
                print("Username can't be empty.")

            elif store_user_name.isdigit():
                print("Username should at least one letter.")
            elif len(store_user_name) < 4:
                print("Username should be at least 4 character long.")

            else:
                user_pass["Username"].append(store_user_name)
                print("Your Username is added.")
                break

        while True:
            store_user_password = input("Enter Your Password: ").strip()
            if not store_user_password:
                print("Password can't be empty.")
            elif not store_user_password.isdigit():
                print("Password should be in number only.")
            elif len(store_user_password) < 5:
                print("The length of Password should be at least 5")

            else:
                user_pass["Password"].append(store_user_password)
                print("Your Password is added.")
                break

    # TO login
    elif choice == "2":
        check_user_name = input("Enter Your Username: ").strip()
        check_user_password = input("Enter Your Password: ").strip()

        login_success = check_user_name in user_pass["Username"] and check_user_password in user_pass["Password"]

        if login_success:
            print("Login Successful.")

        elif check_user_name not in user_pass["Username"]:
            print("User not found.")
        elif check_user_password not in user_pass["Password"]:
            print("Incorrect Password.")
        else:
            print("Hello")


    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Please press 1,2 or 3 to move forward.")



