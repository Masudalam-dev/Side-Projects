# To find the number if it is positive Negative or Zero
# Use at least one boolean variable

user_num = int(input("Enter a Num: "))
number = False
if user_num == 0:
    print("Zero")
elif user_num >= 1:
    number = True
    if number:
        print("Positive")
else:
    print("Negative")

# This is more clean version suggested by GPT
# user_num = int(input("Enter a Num: "))
# is_positive = user_num > 0
#
# if user_num == 0:
#     print("Zero")
# elif is_positive:
#     print("Positive")
# else:
#     print("Negative")