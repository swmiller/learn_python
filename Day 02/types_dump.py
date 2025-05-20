message = "Hello"

# Subscripting
print("First chacter: " +message[0])
print("Last chacter: " +message[4])

# Negative index trick
print("Last chacter trick: " +message[-1])

# Concatenation (doesn't add numbers)
print ("Concatenation: " + "123" + "456")

# Iterating over a string
print("Iterating over a string:")
for char in message:
    print(char)

# Integer - whole number
print("Integer:", 123 + 456)

# Integer - psuedo commas
print("Big integer", 123_456_789)

# Float - a number with a decimal point
print("Float:", 123.456)

# Boolean - True or False
print("Boolean:", True)
print("Boolean:", False)

# Type function
print("Type of 123:", type(123))
print("Type of 123.456:", type(123.456))
print("Type of True:", type(True))
print("Type of False:", type(False))
print("Type of 'Hello':", type("Hello"))

# Define a class
class MyClass:
    pass

# Create an instance of the class
my_instance = MyClass()

# Print the type of the instance
print("Type of my_instance:", type(my_instance))

# Type casting
print("Type casting:", int("123") + 456)

# Doesn't work
#print("Number of letters in your name: " + (len(input("What is your name? "))))

# Works
print("Number of letters in your name: " + str(len(input("What is your name? "))))