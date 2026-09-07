# CLI Quiz Game
# Command-Line Based Quiz Application

questions = [
    {
        "question": "What is the capital city of Kenya?",
        "choices": {
            "A": "Mombasa",
            "B": "Nairobi",
            "C": "Kisumu",
            "D": "Nakuru"
        },
        "answer": "B"
    },

    {
        "question": "Which programming language are we using?",
        "choices": {
            "A": "Java",
            "B": "C++",
            "C": "Python",
            "D": "PHP"
        },
        "answer": "C"
    },

    {
        "question": "What does CPU stand for?",
        "choices": {
            "A": "Central Processing Unit",
            "B": "Computer Personal Unit",
            "C": "Central Program Unit",
            "D": "Computer Processing Unit"
        },
        "answer": "A"
    },

    {
        "question": "How many bits are in one byte?",
        "choices": {
            "A": "4",
            "B": "8",
            "C": "16",
            "D": "32"
        },
        "answer": "B"
    },

    {
        "question": "Which of these is an operating system?",
        "choices": {
            "A": "Python",
            "B": "Windows",
            "C": "HTML",
            "D": "MySQL"
        },
        "answer": "B"
    }
]


# Starting score
score = 0


# Display title
print("==============================")
print("       CLI QUIZ GAME")
print("==============================")
print()


# Display questions one by one
for number, question in enumerate(questions, start=1):

    print(f"Question {number}: {question['question']}")

    # Display choices
    for letter, choice in question["choices"].items():
        print(f"{letter}. {choice}")

    # Get user's answer
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    # Check the answer
    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question["answer"])

    print()


# Display final score
print("==============================")
print("        QUIZ FINISHED")
print("==============================")

print("Your score:", score, "/", len(questions))
if score ==len(questions):
    print("feedback:Excellent!")
elif score>=len(questions)/2:
    print("feedback:Good!")
else:
    print("feedback:Try again!")
