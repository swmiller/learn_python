import os
from data import MENU, resources, COINS


# Coffee machine Requirements:
# 1 Make three hot flavors:
#   1.1 Espresso
#       1.1.1 Ingredients: 50ml water, 18g coffee
#       1.1.2 Price: $1.50
#   1.2 Latte
#       1.2.1 Ingredients: 200ml water, 24g coffee, 150ml milk
#       1.2.2 Price: $2.50
#   1.3 Cappuccino
#       1.3.1 Ingredients: 250ml water, 24g coffee, 100ml milk
#       1.3.2 Price: $3.00
# 2. Resources:
#   2.1 Water: 300ml
#   2.2 Milk: 200ml
#   2.3 Coffee: 100g
# 3. Coin Operated:
#   3.1 Coins: quarters, dimes, nickels, pennies
#       3.1.1 Quarters: 25 cents
#       3.1.2 Dimes: 10 cents
#       3.1.3 Nickels: 5 cents
#       3.1.4 Pennies: 1 cent
# 4. Operation Requirements:
#    4.1 Report on resources left in the machine
#    4.2 Allow selection of drink
#        4.2.1 If resources are not available report that drink is not available and allow for different selection
#    4.3 Allow user to insert coins
#    4.4 Give change if needed
#    4.5 Make the drink and update the resource counts


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_user_selection():
    options = list(MENU.keys())
    while True:
        print("\nPlease select a drink:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        choice = input("Enter the number of your choice: ").strip().lower()
        if choice == "shutdown":
            return "shutdown"
        elif choice == "report":
            return "report"
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        else:
            print("Invalid selection. Please try again.")


def get_coffee_cost(product):
    return MENU[product]["cost"]


def get_coffee_ingredients(product):
    return MENU[product]["ingredients"]


def process_coins(coffee_product_price):
    print(f"Please insert coins to pay for your ${coffee_product_price:.2f} coffee.")
    total = 0.0
    while total < coffee_product_price:
        print(
            f"Current total: ${total:.2f}. Amount remaining: ${coffee_product_price - total:.2f}"
        )
        for coin, value in COINS.items():
            while True:
                try:
                    amount = int(input(f"How many {coin}?: "))
                    if amount < 0:
                        raise ValueError("Amount cannot be negative.")
                    total += amount * value
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid number.")
        if total >= coffee_product_price:
            break
    print(f"Total inserted: ${total:.2f}")
    return total


def check_resources(coffee_product):
    ingredients = get_coffee_ingredients(coffee_product)
    for item, amount in ingredients.items():
        if resources[item] < amount:
            return False
    return True


def report_menu():
    # clear_screen()
    print("Current resources:")
    for item, amount in resources.items():
        print(
            f"{item.capitalize()}: {amount}ml"
            if item != "coffee"
            else f"{item.capitalize()}: {amount}g"
        )


def main():
    while True:
        # Get the user select and ensure the ingredients are available
        user_selection = None
        while True:
            user_selection = get_user_selection()
            if user_selection == "report":
                report_menu()
                continue
            elif user_selection == "shutdown":
                print("Shutting down the coffee machine.")
                return
            elif not check_resources(user_selection):
                print(
                    f"Sorry, we don't have enough resources to make {user_selection}. Please select a different drink."
                )
                continue
            else:
                break

        # Collect payment for the coffee product
        coffee_product_price = get_coffee_cost(user_selection)
        amount_paid = process_coins(coffee_product_price)
        if amount_paid > coffee_product_price:
            change = amount_paid - coffee_product_price
            print(f"Here is your change: ${change:.2f}")

        # Deduct the ingredients from the resources
        ingredients = get_coffee_ingredients(user_selection)
        for item, amount in ingredients.items():
            resources[item] -= amount

        # Serve the coffee
        print(f"Here is your {user_selection}. Enjoy!")


if __name__ == "__main__":
    main()
