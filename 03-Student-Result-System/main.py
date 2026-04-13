
def student_score():
    student_name = input("Enter your Name:\n")

    physics = int(input("Enter your Physics marks:\n"))
    chemistry = int(input("Enter your Chemistry marks:\n"))
    math = int(input("Enter your math marks:\n"))
    sst = int(input("Enter your Social Science marks:\n"))
    english = int(input("Enter your English marks:\n"))

    marks = [physics,chemistry,math,sst,english]
    total_marks = sum(marks)
    average_marks = total_marks / 5

    fail = False
    for m in marks:
        if m < 33:
            fail = True
            break
    print("\n******* Result *********")
    print(f"Name: {student_name}")
    print(f"Total marks: {total_marks}")
    print(f"Average marks: {average_marks}")

    if fail:
        print("Result: Fail(Less than 33 marks in a subject).")
    else:
        if average_marks > 90:
            print("Grade A")
        elif 70 <= average_marks <= 89:
            print("Grade B")
        elif 50 <= average_marks <= 69:
            print("Grade C")
        else:
            print("Fail")

while True:
    student_score()

    choice = input("\nDo you want to check another student? (yes/no): ").lower()

    if choice != "yes":
        print("Have a nice day!")
        break

