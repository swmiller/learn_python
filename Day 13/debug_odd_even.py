def odd_or_even(number):
    if (
        number % 2 == 0
    ):  # This line had a syntax error. The correct operator is '==' for comparison and not = for assignment.
        return "This is an even number."
    else:
        return "This is an odd number."
