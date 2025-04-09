import random

word_list = ["aardvark", "baboon", "camel"]
max_guesses = 6


def gallows_default():
    return """
  +---+
      |
      |
      |
      |
      |
=========
"""


def gallows_wrong_guess_1():
    return """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""


def gallows_wrong_guess_2():
    return """
  +---+
  |   |
  O   |
 /    |
      |
      |
=========
"""


def gallows_wrong_guess_3():
    return """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""


def gallows_wrong_guess_4():
    return """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
"""


def gallows_wrong_guess_5():
    return """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
"""


def gallows_wrong_guess_6():
    return """
  +---+
  |   |
  O   |
 /|\\  |
 / \  |
      |
=========
"""


gallows_switch = {
    1: gallows_wrong_guess_1,
    2: gallows_wrong_guess_2,
    3: gallows_wrong_guess_3,
    4: gallows_wrong_guess_4,
    5: gallows_wrong_guess_5,
    6: gallows_wrong_guess_6,
}


def print_gallows(wrong_guess_count):
    gallows_result = gallows_switch.get(
        wrong_guess_count, gallows_default
    )()  # Call the function
    print(gallows_result)


def get_user_guess():
    while True:
        guess = input("\nGuess a letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Invalid input. Please enter a single letter.")


def print_chosen_word(chosen_word, guesses):
    display = ""
    for letter in chosen_word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    print(" ".join(display))


def main():
    # Randomly choose a word from the word_list
    chosen_word = random.choice(word_list)

    wrong_guesses = 0
    guessed_letters = []
    while True:
        print_gallows(wrong_guesses)
        print_chosen_word(chosen_word, guessed_letters)

        user_guess = get_user_guess()
        if user_guess not in guessed_letters:
            guessed_letters.append(user_guess)

        if not user_guess in chosen_word:
            # Wrong
            wrong_guesses += 1

        if wrong_guesses == max_guesses:
            print_gallows(wrong_guesses)
            print("\nGame over! The word was:", chosen_word)
            break

        if all(letter in guessed_letters for letter in chosen_word):
            print("\nCongratulations! You've guessed the word:", chosen_word)
            break


if __name__ == "__main__":
    main()
