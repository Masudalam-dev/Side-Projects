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


            # print("Password should be in number.")
            # store_user_password = input("Enter Your Password: ").strip()
            # if store_user_password.isdigit():
            #     user_pass["Password"].append(store_user_password)
            #     print("Your Password is added.")
            #     break
            # else:
            #     print("Please make password in digit only.")

    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Please press 1,2 or 3 to move forward.")

    # check_user_name = input("Enter Your Username: ").strip()
    #
    # if check_user_name in user_pass["Username"]:
    #     print("Correct username")
    # else:
    #     print("User not found.")
    #
    # chek_user_password = input("Enter Your Password: ").strip()
    # if chek_user_password in user_pass["Password"]:
    #     print("Correct password")
    # else:
    #     print("Incorrect Password.")

