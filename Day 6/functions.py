def do_something():
    print("This is the 'do_something()' function")


def get_user_name():
    name = input("Enter your name: ")
    print(f"Hello, {name}")


def main():
    do_something()
    get_user_name()


if __name__ == "__main__":
    main()
