programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving a value
print(programming_dictionary["Bug"])

# Adding a new key-value pair
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Updating an existing key-value pair
programming_dictionary["Bug"] = "A mistake in the code."

# Removing a key-value pair
del programming_dictionary["Function"]

# Checking if a key exists
if "Loop" in programming_dictionary:
    print("Loop is in the dictionary.")

# Iterating through keys
for key in programming_dictionary:
    print(key)

# Iterating through values
for value in programming_dictionary.values():
    print(value)

# Iterating through key-value pairs
for key, value in programming_dictionary.items():
    print(f"{key}: {value}")

# Clearing the dictionary
programming_dictionary.clear()
print(programming_dictionary)


