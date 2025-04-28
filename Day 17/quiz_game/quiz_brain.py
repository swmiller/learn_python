# Note: I implemented this differently from what Dr. Yu did. It seemed to make sense to have a "play" method
# that would drive the quiz game.
#
# Also, I suppose the creation of the question bank could be delegated to this class as well.
class QuizBrain:
    def __init__(self, question_list):
        """
        Initializes the QuizBrain instance with a list of questions.

        Args:
            question_list (list): A list of Question objects.
        """
        self.__question_number = 0
        self.__score = 0
        self.__question_list = question_list

    def __get_user_answer(self):
        """
        Prompts the user for an answer (True/False) and validates the input.
        This is a private method.

        Returns:
            bool: The user's answer as a boolean.
        """
        while True:
            user_input = input("(true/false): ").strip().lower()
            if user_input == "true":
                return True
            elif user_input == "false":
                return False
            else:
                print("Invalid input. Please enter 'true' or 'false'.")

    def play(self):
        """
        Executes the quiz game by iterating through the list of questions,
        prompting the user for answers, and providing feedback on correctness.

        Attributes:
            question_number (int): Tracks the current question number.
            score (int): Tracks the user's score during the game.

        Behavior:
            - Displays each question to the user.
            - Collects the user's answer using a private method.
            - Compares the user's answer to the correct answer.
            - Updates the score if the user's answer is correct.
            - Provides feedback on whether the user's answer was correct or incorrect.
            - Displays the correct answer if the user's answer was incorrect.
            - Prints the final score after all questions have been answered.
        """

        while self.__question_number < len(self.__question_list):
            print(
                f"Q.{self.__question_number + 1}: {self.__question_list[self.__question_number].text} ",
                end="",
            )
            self.__question_number += 1
            user_answer = self.__get_user_answer()
            if user_answer == self.__question_list[self.__question_number - 1].answer:
                print("You got it right!")
                self.__score += 1
            else:
                print("That's wrong.")
                print(
                    f"The correct answer was: {self.__question_list[self.__question_number - 1].answer}"
                )
            print()

        percentage_score = (self.__score / self.__question_number) * 100
        print(
            f"Finished! Your score is: {self.__score}/{self.__question_number} ({percentage_score:.2f}%)"
        )
