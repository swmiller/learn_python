from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import os

# Constants
QUESTION_KEY = "text"
ANSWER_KEY = "answer"
TRUE_VALUE = "true"

# Global Variables
question_bank = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def create_question_bank(data):
    for question in data:
        question_text = question[QUESTION_KEY]
        answer_text = question[ANSWER_KEY].lower() == TRUE_VALUE
        question_bank.append(Question(question_text, answer_text))


if __name__ == "__main__":
    clear_screen()
    print("Welcome to the Quiz!")

    create_question_bank(question_data)
    # for question in question_bank:
    #     print(f"Q: {question.text} | A: {question.answer}")

    quiz = QuizBrain(question_bank)
    quiz.play()
