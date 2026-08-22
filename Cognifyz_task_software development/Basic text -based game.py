def quiz_game():
    print("=" * 45)
    print("        WELCOME TO THE PYTHON QUIZ")
    print("=" * 45)

    score = 0

    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. def", "C. fun", "D. define"],
            "answer": "B",
        },
        {
            "question": "Which data type stores True or False values?",
            "options": ["A. String", "B. Integer", "C. Boolean", "D. List"],
            "answer": "C",
        },
        {
            "question": "Which symbol is used for single-line comments in Python?",
            "options": ["A. //", "B. /* */", "C. #", "D. --"],
            "answer": "C",
        },
        {
            "question": "Which function is used to display output on the screen?",
            "options": [
                "A. display()",
                "B. print()",
                "C. output()",
                "D. show()",
            ],
            "answer": "B",
        },
        {
            "question": "Which data structure is ordered and immutable (cannot be changed)?",
            "options": [
                "A. List",
                "B. Dictionary",
                "C. Set",
                "D. Tuple",
            ],
            "answer": "D",
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .pyth", "B. .pt", "C. .py", "D. .p"],
            "answer": "C",
        },
        {
            "question": "Which function is used to take input from the user?",
            "options": [
                "A. scan()",
                "B. input()",
                "C. get()",
                "D. read()",
            ],
            "answer": "B",
        },
        {
            "question": "What is the output of len('Python')?",
            "options": ["A. 5", "B. 6", "C. 7", "D. Error"],
            "answer": "B",
        },
        {
            "question": "Which operator is used for exponentiation (power) in Python?",
            "options": ["A. ^", "B. **", "C. ^^", "D. //"],
            "answer": "B",
        },
        {
            "question": "Which collection type stores key-value pairs?",
            "options": [
                "A. List",
                "B. Tuple",
                "C. Dictionary",
                "D. Set",
            ],
            "answer": "C",
        },
    ]

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for option in q["options"]:
            print(f"   {option}")

        while True:
            user_choice = input("\nEnter your answer (A/B/C/D or Q to quit): ").strip().upper()

            if not user_choice:
                print("❌ No option selected! Please choose A, B, C, or D.")
                continue

            if user_choice in {"Q", "QUIT", "EXIT"}:
                print("\nQuiz ended by the player.")
                print("\n" + "=" * 45)
                print("                QUIZ RESULT")
                print("=" * 45)
                print(f"Final Score: {score} out of {len(questions)}")
                if len(questions) > 0:
                    percentage = (score / len(questions)) * 100
                    print(f"Percentage: {percentage:.1f}%")
                print("=" * 45)
                return

            if user_choice not in ["A", "B", "C", "D"]:
                print(f"❌ Invalid choice '{user_choice}' entered! Please use A, B, C, or D.")
                continue

            if user_choice == q["answer"]:
                print(f"✅ Correct! You chose '{user_choice}'.")
                score += 1
            else:
                print(
                    f"❌ Wrong! You chose '{user_choice}', but the correct answer is '{q['answer']}'."
                )
            break

    print("\n" + "=" * 45)
    print("                QUIZ RESULT")
    print("=" * 45)
    print(f"Final Score: {score} out of {len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")

    if score == 10:
        print("Rating: Excellent! Perfect score!")
    elif score >= 7:
        print("Rating: Good job!")
    elif score >= 4:
        print("Rating: Needs improvement.")
    else:
        print("Rating: Keep practicing!")
    print("=" * 45)


if __name__ == "__main__":
    quiz_game()