# Function with now inputs
# def greet():
#     print("Hello")
#     print("How are you?")
#     print("Isn't the weather nice?")


# greet()
# print()


# Function with an input
# def greet_with_name(name):
#     print(f"Hello, {name}!")
#     print(f"How are you, {name}?")
#     print("Isn't the weather nice?")


# greet_with_name("Alice")
# print()


# Function with multiple inputs
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")


greet_with("Alice", "New York")
print()

# Keyword arguments
greet_with(location="London", name="Charles")
print()
