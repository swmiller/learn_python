while True:
    try:
        age = int(input("How old are you? "))
        if age > 18:
            print(f"You can drive at age {age}.")
        else:
            print(f"You cannot drive at age {age}.")
        break
    except ValueError:
        print("Please enter a valid number.")
