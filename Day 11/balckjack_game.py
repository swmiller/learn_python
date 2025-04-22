from art import logo
import random
import os
import platform


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# This function is used to deal a card from the deck
def deal_card():
    return random.choice(cards)


# This function checks if the player or dealer has a blackjack
def has_blackjack(cards):
    """Check if the hand is a blackjack (21 points with exactly 2 cards)"""
    return sum(cards) == 21 and len(cards) == 2


# This function shows the dealer's cards, hiding the first card if specified
def show_dealer_cards(dealer_hand, hide_first_card=True):
    print("\nDealer's cards: ", end="")
    if hide_first_card:
        print("X", end=" ")  # Hide the first card
        for card in dealer_hand[1:]:
            print(card, end=" ")
        print()
    else:
        for card in dealer_hand:
            print(card, end=" ")
        score = calculate_score(dealer_hand)
        print(f" | Total score: {score}")


# This function shows the player's cards and calculates the score
def show_player_cards(player_hand):
    print("Your cards    : ", end="")
    for card in player_hand:
        print(card, end=" ")
    score = calculate_score(player_hand)
    print(f" | Total score: {score}")


# This function prints the logo of the game
def print_logo():
    print(logo)


# This function checks if the dealer should hit based on their score
def should_dealer_hit(dealer_score):
    # Dealer hits if score is 16 or less
    return dealer_score <= 16


# This function asks the player if they want to hit or stand
def ask_player_action():
    while True:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action in ["h", "s"]:
            return action
        else:
            print("Invalid input. Please enter 'h' for hit or 's' for stand.")


# This function calculates the score of a hand, properly handling Aces
def calculate_score(cards_list):
    # Create a copy to avoid modifying the original list
    cards_copy = cards_list.copy()
    score = sum(cards_copy)

    # Handle Aces (11) if score is over 21
    aces = cards_copy.count(11)
    for _ in range(aces):
        if score > 21:
            cards_copy.remove(11)
            cards_copy.append(1)
            score = sum(cards_copy)

    return score


# This function plays a single game of Blackjack
def play_game():
    print_logo()
    print("Welcome to the Blackjack game!")

    # Deal initial cards
    dealer_hand = [deal_card(), deal_card()]
    player_hand = [deal_card(), deal_card()]

    show_dealer_cards(dealer_hand)
    show_player_cards(player_hand)

    # Check for blackjacks
    player_has_blackjack = has_blackjack(player_hand)
    dealer_has_blackjack = has_blackjack(dealer_hand)

    if player_has_blackjack and dealer_has_blackjack:
        print("Both you and the dealer have blackjack! It's a tie! 😲")
        return
    elif player_has_blackjack:
        print("You have a blackjack! You win! 😀")
        return
    elif dealer_has_blackjack:
        print("Dealer has a blackjack! Dealer wins! 😭")
        return

    # Initialize scores
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # Player's turn
    player_action = ask_player_action()
    while player_action == "h":
        player_hand.append(deal_card())
        show_player_cards(player_hand)
        player_score = calculate_score(player_hand)

        if player_score > 21:
            print("You busted! Dealer wins!")
            return

        player_action = ask_player_action()

    # Dealer's turn
    print("\nDealer's turn:")
    show_dealer_cards(dealer_hand, hide_first_card=False)

    while should_dealer_hit(dealer_score):
        print("Dealer hits.")
        dealer_hand.append(deal_card())
        show_dealer_cards(dealer_hand, hide_first_card=False)
        dealer_score = calculate_score(dealer_hand)

        if dealer_score > 21:
            print("Dealer busted! You win!")
            return

    print("Dealer stands.")

    # Determine the winner
    print("\nFinal Results:")
    show_player_cards(player_hand)
    show_dealer_cards(dealer_hand, hide_first_card=False)

    if dealer_score > player_score:
        print("Dealer wins!")
    elif dealer_score < player_score:
        print("You win!")
    else:
        print("It's a tie!")


# This function clears the console screen
def clear_screen():
    """Clears the console screen."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# This function is the main entry point of the program
def main():
    clear_screen()
    while True:
        play_game()

        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
        print("\n" + "-" * 50 + "\n")


# This is the main function that starts the game
if __name__ == "__main__":
    main()
