def main():
    print("Welcome to the rollercoaster ticket booth!")
    bill = 0

    # Get user's height
    your_height = int(input("Enter your height in inches: "))

    if your_height >= 120:
        print("You are tall enough to ride the roller coaster!")

        # Get user's age
        your_age = int(input("Enter your age: "))

        # Determine ticket price based on age
        if your_age < 12:
            ticket_price = 5
        elif 12 <= your_age < 18:
            ticket_price = 7
        elif your_age >= 45 and your_age <= 55:
            ticket_price = 0
        else:
            ticket_price = 12

        print(f"The ticket price based on your age is ${ticket_price}.")
        bill += ticket_price

        # Check if the user wants a photo
        wants_photo = input("Do you want a photo taken? Y or N: ").strip().upper()
        if wants_photo == "Y":
            bill += 3

        print(f"Your final bill is ${bill}.")
    else:
        print("Sorry, you are not tall enough to ride the roller coaster.")
        print("Here, have a lollipop to cheer you up!")


if __name__ == "__main__":
    main()
