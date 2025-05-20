import random

print("Welcome to the PyPassword Generaotr!")
letters = int(
    input("How mant letters would you like in your password? ")
)  # ascii 65 - 122
symbols = int(input("Hom many symbols would you like? "))  # ascii 33 - 47
numbers = int(input("How many numbers would you like? "))  # ascii 48 - 57

# Calculate the total length of the password
password_length = letters + symbols + numbers

# Generate a password of pwassword_length. Include the count of letters, symbols and numbers. Letters should be from 65 - 122, symbols from 33 - 47 and numbers from 48 - 57.
password = ""
for i in range(letters):
    password += chr(random.randint(65, 122))
for i in range(symbols):
    password += chr(random.randint(33, 47))
for i in range(numbers):
    password += chr(random.randint(48, 57))

# Shuffle the password
password = list(password)
random.shuffle(password)
password = "".join(password)

# Print the password
print(f"Your password is: {password}")
