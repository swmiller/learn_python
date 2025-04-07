def main():
    print("Welcome to Python Pizza Deliveries!")

    # Get pizza size
    while True:
        size = input("What size pizza do you want? S, M, or L: ").upper()
        if size in ["S", "M", "L"]:
            break
        print("Invalid input. Please enter S, M, or L.")

    # Ask for pepperoni
    while True:
        add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
        if add_pepperoni in ["Y", "N"]:
            break
        print("Invalid input. Please enter Y or N.")

    # Ask for extra cheese
    while True:
        extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
        if extra_cheese in ["Y", "N"]:
            break
        print("Invalid input. Please enter Y or N.")

    # Calculate the bill
    bill = 0

    if size == "S":
        bill += 15
        if add_pepperoni == "Y":
            bill += 2
    elif size == "M":
        bill += 20
        if add_pepperoni == "Y":
            bill += 3
    elif size == "L":
        bill += 25
        if add_pepperoni == "Y":
            bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}.")


if __name__ == "__main__":
    main()
