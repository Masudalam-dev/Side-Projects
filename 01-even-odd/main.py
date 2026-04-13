# find even-odd using variable value as True or False
# user_num = int(input("Enter any num: "))
# num_is_not_divisible_by_two = False
# if user_num % 2 != 0:
#     num_is_not_divisible_by_two = True
# if  num_is_not_divisible_by_two:
#     print("Odd")
# else:
#     print("Even")

# Finding even odd using (not)
# user_num = int(input("Enter any num: "))
# num_div_by_two = False
# if user_num % 2 == 0:
#     num_div_by_two = True
#
# if not num_div_by_two:
#     print("Odd")
# else:
#     print("Even")


# Better Version
user_num = int(input("Enter a Number: "))
num_div_by_two = (user_num % 2 == 0)
if not num_div_by_two:
    print("Odd")
else:
    print("Even")
