# 1 store questions and correct answer
print("Welcome to Game of quiz!\n")

quiz = {
    "q1": {
        "question": "01.What is the result of 0.1 + 0.2 == 0.3?",
        "options": ["A) True", "B) False", "C) None", "D) SyntaxError"],
        "answer": "B) False",
        "correct_answer": "b"
    },

    "q2": {
        "question": "02.How do you calculate 2 to the power of 3 (2³) in Python?",
        "options": ["A) 2 ^ 3", "B) 2 ** 3", "C) 2 x 3", "D) math.power(2, 3)"],
        "answer": "B) 2 ** 3",
        "correct_answer": "b"
    },

    "q3": {
        "question": "03.How do you add 'apple' to the end of a list called fruits?",
        "options": ["A) fruits.add('apple')", "B) fruits.push('apple')", "C) fruits.append('apple')", "D) fruits + 'apple'"],
        "answer": "C) fruits.append('apple')",
        "correct_answer": "c"
    },

    "q4": {
        "question": "04.Which symbol do you use to write a comment in Python?",
        "options": ["A) //", "B) /*", "C) --", "D) #"],
        "answer": "D) #",
        "correct_answer": "d"
    },

    "q5": {
        "question": "05.What is the standard naming style for variables in Python (like my_variable)?",
        "options": ["A) snake_case", "B) camelCase", "C) PascalCase", "D) SCREAMING_SNAKE_CASE"],
        "answer": "A) snake_case",
        "correct_answer": "a"
    }
}

# 2 ask question one by one
score = 0
wrong_score = 0
for q in quiz.values():
    print(q["question"])
    for option in q["options"]:
        print(option)

# 03 check Answer
    user_ans = input("Choose the correct options: \n").strip()
    if user_ans.lower() == q["correct_answer"]:
        print("Correct ✅")
        score += 1
    else:
        print(f"Wrong ❌ | Correct Ans: {q['answer']}")
        wrong_score += 1


# 04 Final Result
percentage = (score/len(quiz))* 100
print(f"You answered correctly: {score} question.")
print(f"You answered wrong: {wrong_score} question.")
print(f"Your final Score: {percentage} percentage.")
