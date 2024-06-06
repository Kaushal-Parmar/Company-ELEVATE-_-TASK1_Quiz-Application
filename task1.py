import random

questions = [
    {
        "question": "What is the capital of India ?",
        "choices": ["A. Delhi", "B. Gujarat", "C. Punjab", "D.Goa  "],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Jane Austen"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    }
]

def ask_question(question):
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    answer = input("Enter your answer (A, B, C, or D): ").upper()
    while answer not in ['A', 'B', 'C', 'D']:
        answer = input("Invalid input. Please enter A, B, C, or D: ").upper()
    return answer == question["answer"]

def run_quiz():
    print("-----------Welcome to the Quiz!-----------")
    print("Answer the following questions by entering the letter corresponding to your choice.\n")

    score = 0
    random.shuffle(questions)

    for question in questions:
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {question['answer']}.\n")

    print(f"Quiz over! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()
