import os
from art import logo

# Dictionary to store bids
bids = {}


# Function to clear the terminal screen based on the operating system
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Function to print the auction logo and welcome message
def print_logo():
    print(logo)
    print("Welcome to the Silent Auction!")


# Function to add a bid to the bids dictionary
def add_bid(name: str, bid: float):
    bids[name] = bid


# Function to determine the highest bidder and their bid amount
def get_highest_bidder():
    if not bids:
        return None, 0
    highest_bidder = max(bids, key=bids.get)
    return highest_bidder, bids[highest_bidder]


# Main function to run the auction
if __name__ == "__main__":
    print_logo()

    while True:
        name = input("Enter your name: ")
        bid = float(input("Enter your bid: $"))
        add_bid(name, bid)

        more_bidders = input(
            "Are there any other bidders? Type 'yes' or 'no': "
        ).lower()
        if more_bidders == "no":
            break
        else:
            clear_screen()

    winner, highest_bid = get_highest_bidder()

    clear_screen()
    if winner:
        print(f"The winner is {winner} with a bid of ${highest_bid:.2f}")
    else:
        print("No bids were placed.")
