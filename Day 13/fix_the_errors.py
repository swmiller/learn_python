age = int(input("How old are you?"))
if age > 18:
    # Print statement was not originally indented correctly
    print(
        f"You can drive at age {age}."
    )  # Orignall printed "{age} instead of the number entered by the user. The "f" was missing.
