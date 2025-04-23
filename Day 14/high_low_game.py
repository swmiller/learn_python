from art import logo
from art import vs
from game_data import data
import random


def is_guess_correct(guess, option_1, option_2):
    if (guess == 1 and option_1["follower_count"] > option_2["follower_count"]) or (
        guess == 2 and option_2["follower_count"] > option_1["follower_count"]
    ):
        return True
    return False


def get_user_guess():
    while True:
        try:
            guess = int(input("Which one has more followers? Type '1' or '2': "))
            if guess in [1, 2]:
                return guess
            else:
                print("Invalid input. Please type '1' or '2'.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def get_two_options():
    option_1_number = random.randint(0, len(data) - 1)
    option_2_number = random.randint(0, len(data) - 1)
    while option_1_number == option_2_number:
        option_2_number = random.randint(0, len(data) - 1)

    option_1 = data[option_1_number]
    option_2 = data[option_2_number]

    return option_1, option_2


def print_options(option_1, option_2):
    print(
        f"\n1: {option_1['name']}, a {option_1['description']}, from {option_1['country']}"
    )
    print(vs)
    print(
        f"2: {option_2['name']}, a {option_2['description']}, from {option_2['country']}"
    )


def main():
    print(logo)
    print("Welcome to the High-Low Game!")

    score = 0
    game_over = False

    # 1. Game picks two random pieces of data
    option_1, option_2 = get_two_options()

    while not game_over:
        # 2. Game presents the user with option A and option B
        print_options(option_1, option_2)

        # 3. User guesses which one has more followers
        guess = get_user_guess()

        # 4. Game checks if the guess is correct
        if is_guess_correct(guess, option_1, option_2):
            # 5. If correct, the game continues with a new piece of data and awards the user a point
            score += 1
            print(f"Correct! Your score is now {score}.")
            option_1, option_2 = get_two_options()
        else:
            # 6. If incorrect, the game ends and the user is shown their score
            game_over = True
            print(f"Wrong! Your final score is {score}.")


if __name__ == "__main__":
    main()
