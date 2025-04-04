# TypeError: object of type 'int' has no len()
# number_length = len(123454)

# This works
print(len(str(123454)))

# Print the data type
print(type("Hello"))

# Data types learned
print("\nData types learned:")
print(type("Hello"))
print(type(123))
print(type(123.456))
print(type(True))

# Convert data types
print("\nConvert data types:")
int_to_conver = 123456789
convert_to_str = str(int_to_conver)
print("Convert to string:", convert_to_str)

float_to_convert = 123.456
convert_to_int = int(float_to_convert)
print("Convert to int:", convert_to_int)

bool_to_convert = True
convert_to_int = int(bool_to_convert)
print("Convert to int:", convert_to_int)

# Code challenge
print("\nCode challenge:")
# TypeError: object of type 'int' has no len()
# This line will cause an error because len() cannot be applied to an integer
#print("Number of letters in your name: " + len(input("What is your name? ")))

# This line will work because we convert the integer to a string first
print("Number of letters in your name: " + str(len(input("What is your name? "))))
