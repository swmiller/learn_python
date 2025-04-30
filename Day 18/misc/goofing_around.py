def main():
    print("Hello, World!")
    while True:
        response = prompt_user()
        if response == "no":
            print("Goodbye!")
            break
        number = int(input("Enter a number to check if it's prime: "))
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")


def prompt_user():
    while True:
        response = input("Do you want to continue? (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return response
        print("Invalid input. Please enter 'yes' or 'no'.")


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
