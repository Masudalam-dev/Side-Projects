# 1 store questions and correct answer
quiz = {
    "q1": {
        "question": "What is the result of 0.1 + 0.2 == 0.3?",
        "options": ["A) True", "B) False", "C) None", "D) SyntaxError"],
        "answer": "B) False"
    },

    "q2": {
        "question": "How do you calculate 2 to the power of 3 (2³) in Python?",
        "options": ["A) 2 ^ 3", "B) 2 ** 3", "C) 2 x 3", "D) math.power(2, 3)"],
        "answer": "B) 2 ** 3"
    },

    "q3": {}
}




question = ["What is the result of 0.1 + 0.2 == 0.3?",
            "How do you calculate 2 to the power of 3 (2³) in Python?",
            "How do you add 'apple' to the end of a list called fruits?",
            "Which symbol do you use to write a comment in Python?",
            "What is the standard naming style for variables in Python (like my_variable)?",
            ]
answer = ["False", "2 ** 3", "fruits.append('apple')", "#", "snake_case"]

print(quiz["q1"]["question"])
for i in quiz["q1"]["options"]:
    print(i)

user_input = input("Enter the right option.")
if user_input.lower() == "b":
    print("Well done ✅")
else:
    print(f"Correct answer: {quiz["q1"]["answer"]}")