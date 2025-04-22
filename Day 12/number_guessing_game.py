import random
from art import logo

NUMBER_OF_GUESSES_EASY = 10
NUMBER_OF_GUESSES_HARD = 5


def pick_number():
    return random.randint(1, 100)


def get_difficulty():
    while True:
        difficulty = (
            input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        )
        if difficulty in ["easy", "hard"]:
            return difficulty
        print("Invalid choice. Please type 'easy' or 'hard'.")


def print_banner():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def get_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print_banner()
    number_to_guess = pick_number()
    difficulty = get_difficulty()

    attempts = (
        NUMBER_OF_GUESSES_EASY if difficulty == "easy" else NUMBER_OF_GUESSES_HARD
    )

    for i in range(attempts):
        print(f"\nYou have {attempts - i} attempts remaining to guess the number.")
        guess = get_guess()
        if guess == number_to_guess:
            print(f"You got it! The answer was {number_to_guess}.")
            break
        elif guess < number_to_guess:
            print("Too low.")
        else:
            print("Too high.")

    print("\nYou ran out of guesses. You lose.")
    print(f"The number was {number_to_guess}.")


if __name__ == "__main__":
    main()
