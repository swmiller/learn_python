a = 10
b = 5

# Print examples use f-string
# https://realpython.com/python-f-strings/

# Print the values of a and b
print(f"a = {a}")
print(f"b = {b}")

# Addition
addition = a + b
print(f"Addition: {a} + {b} = {addition}")

# Subtraction
subtraction = a - b
print(f"Subtraction: {a} - {b} = {subtraction}")

# Multiplication
multiplication = a * b
print(f"Multiplication: {a} * {b} = {multiplication}")

# Division
division = a / b
print(f"Division: {a} / {b} = {division}")

# Modulus
modulus = a % b
print(f"Modulus: {a} % {b} = {modulus}")

# Exponentiation
exponentiation = a ** b
print(f"Exponentiation: {a} ** {b} = {exponentiation}")

# Floor Division
floor_division = a // b
print(f"Floor Division: {a} // {b} = {floor_division}")

# Operator Precedence
result_1 = a + b * 2
print(f"Operator Precedence (a + b * 2): {result_1}")

result_2 = (a + b) * 2
print(f"Operator Precedence ((a + b) * 2): {result_2}")

result_3 = a + b / 2
print(f"Operator Precedence (a + b / 2): {result_3}")

result_4 = (a + b) / 2
print(f"Operator Precedence ((a + b) / 2): {result_4}")

# Addition Assignment
a += b
print(f"Addition Assignment (a += b): {a}")

# Subtraction Assignment
a -= b
print(f"Subtraction Assignment (a -= b): {a}")

# Multiplication Assignment
a *= b
print(f"Multiplication Assignment (a *= b): {a}")

# Division Assignment
a /= b
print(f"Division Assignment (a /= b): {a}")