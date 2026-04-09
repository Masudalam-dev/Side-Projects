# Question 1
# To find the number if it is positive Negative or Zero
# Use at least one boolean variable

# user_num = int(input("Enter a Num: "))
# number = False
# if user_num == 0:
#     print("Zero")
# elif user_num >= 1:
#     number = True
#     if number:
#         print("Positive")
# else:
#     print("Negative")

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


# Question: 2

user_num = int(input("Enter a num:\n"))
is_positive = user_num > 0
is_negative = user_num < 0
is_even = user_num % 2 == 0
is_odd = user_num % 2 != 0

if is_positive and is_even:
    print("Even Positive")
elif is_positive and is_odd:
    print("Odd Positive")
elif is_negative and is_even:
    print("Even Negative")
elif is_negative and is_odd:
    print("Odd Negative")
else:
    print("Zero")



# By chatGPT
user_num = int(input("Enter a num:\n"))

is_positive = user_num > 0
is_negative = user_num < 0
is_even = user_num % 2 == 0

if is_positive and is_even:
    print("Even Positive")
elif is_positive and not is_even:
    print("Odd Positive")
elif is_negative and is_even:
    print("Even Negative")
elif is_negative and not is_even:
    print("Odd Negative")
else:
    print("Zero")

