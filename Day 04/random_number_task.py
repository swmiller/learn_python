import random
import my_moudle

# Module creation and use
print(f"My favorite number is: {my_moudle.my_favorite_number}")

print(
    f"Random number: {random.randint(1, 100)}"
)  # This line contains a typo in the function name 'print'.

random_number_0_to_1 = random.random()  # Generates a random float between 0.0 and 1.0
print(f"Random number between 0 and 1: {random_number_0_to_1}")

random_number_0_to_1 = (
    random.random() * 10
)  # Generates a random float between 0.0 and 10.0
print(f"Random number between 0 and 1: {random_number_0_to_1}")

random_float = random.uniform(1, 10)  # Generates a random float between 1.0 and 10.0
print(f"Random float between 1 and 10: {random_float}")
