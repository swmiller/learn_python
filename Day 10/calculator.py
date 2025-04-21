from calculator_art import logo
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_logo():
    clear_screen()
    print(logo)
    print("Welcome to the Calculator!")


def get_integer_input(prompt="Enter an integer: "):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_operator_input(prompt="Enter an operator (+, -, *, /): "):
    valid_operators = {"+", "-", "*", "/"}
    while True:
        operator = input(prompt)
        if operator in valid_operators:
            return operator
        else:
            print("Invalid operator. Please enter one of +, -, *, /.")


def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    if num2 == 0:
        raise ValueError("Division by zero is not allowed.")
    return num1 / num2


operations = {
    "+": add_numbers,
    "-": subtract_numbers,
    "*": multiply_numbers,
    "/": divide_numbers,
}


def main():
    display_logo()

    previous_result = None

    while True:
        if previous_result is not None:
            use_previous = (
                input(
                    "Do you want to use the previous result as the first number? (yes/no): "
                )
                .strip()
                .lower()
            )
            if use_previous in {"yes", "y"}:
                num1 = previous_result
            else:
                num1 = get_integer_input("Enter the first number: ")
        else:
            num1 = get_integer_input("Enter the first number: ")

        operator = get_operator_input("Enter an operator (+, -, *, /): ")
        num2 = get_integer_input("Enter the second number: ")

        if operator in operations:
            result = operations[operator](num1, num2)
        else:
            print("Something went wrong. Please try again.")
            continue

        print(f"The result of {num1} {operator} {num2} = {result}")

        previous_result = result

        continue_prompt = (
            input("\nDo you want to perform another calculation? (yes/no): ")
            .strip()
            .lower()
        )
        if continue_prompt not in {"yes", "y"}:
            print("Thank you for using the Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
