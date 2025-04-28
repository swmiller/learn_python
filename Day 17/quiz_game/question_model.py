class Question:
    """
    A class to represent a quiz question.

    Attributes:
        question_text (str): The text of the question.
        answer_text (bool): The correct answer to the question (True or False).

    Methods:
        __init__(text: str, answer: bool):
            Initializes a Question instance with the given text and answer.
    """

    def __init__(self, text: str, answer: bool):
        """
        Initializes a Question instance.

        Args:
            text (str): The text of the question. Must be a non-empty string.
            answer (bool): The correct answer to the question. Must be a boolean value.

        Raises:
            ValueError: If `text` is not a non-empty string.
            ValueError: If `answer` is not a boolean value.
        """

        if not isinstance(text, str) or not text.strip():
            raise ValueError("Parameter (text) must be a non-empty string.")
        if not isinstance(answer, bool):
            raise ValueError(
                "Parameter (answer) must be a boolean value (True or False)."
            )

        self.text = text
        self.answer = answer
