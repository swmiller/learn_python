def format_name(first_name, last_name, reverse=False):
    if not first_name or not last_name:
        return "Invalid input. Please provide both first and last names."

    formatted_name = ""
    if reverse:
        formatted_name = f"{last_name}, {first_name}"
    else:
        formatted_name = f"{first_name} {last_name}"

    return formatted_name.title()


# Example calls to the format_name function
print(format_name("john", "doe"))
print(format_name("jane", "sMith", reverse=True))
print(format_name("alice", "johnson"))
print(format_name("bob", "brown", reverse=True))
print(format_name("", "", False))
