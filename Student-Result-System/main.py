# from turtledemo.round_dance import stop
# def student_score():
#     student_name = input("Enter your Name:\n")
#     physics = int(input("Enter your Physics marks:\n"))
#     chemistry = int(input("Enter your Chemistry marks:\n"))
#     math = int(input("Enter your math marks:\n"))
#     sst = int(input("Enter your Social Science marks:\n"))
#     english = int(input("Enter your English marks:\n"))
#
#     total_marks = physics + chemistry + math + sst + english
#     average_marks = total_marks / 5
#     input_data_in_list = [physics,chemistry,math,sst,english]
#
#     for i in input_data_in_list:
#         if i < 33:
#             print("You have less than 33 marks in your subject:\nFail ")
#             break
#         else:
#             print(f"Name: {student_name}")
#             print(f"Total marks: {total_marks}")
#             print(f"Average marks: {average_marks}")
#             break
#
#     if average_marks > 90:
#         print("Grade A")
#     elif 70 <= average_marks <= 89:
#         print("Grade B")
#     elif 50 <= average_marks <= 69:
#         print("Grade C")
#     else:
#         print("Fail")
#
# student_score()
#
# more_score_check = input("You want to check other student score: Type 'Yes' for continue... or type No to stop!.").lower()
# if more_score_check == "yes":
#     student_score()
# else:
#     stop()
#



student_name = input("Enter your Name:\n")
physics = int(input("Enter your Physics marks:\n"))
chemistry = int(input("Enter your Chemistry marks:\n"))
math = int(input("Enter your math marks:\n"))
sst = int(input("Enter your Social Science marks:\n"))
english = int(input("Enter your English marks:\n"))

total_marks = physics + chemistry + math + sst + english
average_marks = total_marks / 5
marks = [physics,chemistry,math,sst,english]
print(marks)
is_fail = ""
for score_num in marks:
    if score_num < 33:
        is_fail = "Fail"
print(is_fail)


# elif score_num > 33:
# print(f"Total marks: {total_marks}")
# print(f"Average marks: {average_marks}")
# if average_marks > 90:
#     print("Grade A")
# elif 70 <= average_marks <= 89:
#     print("Grade B")
# elif 50 <= average_marks <= 69:
#     print("Grade C")
# else:
#     print("Fail")