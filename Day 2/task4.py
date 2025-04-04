# Rounding
pi = 3.14159
print("The value of pi is:", pi)
print("The value of pi is:", round(pi, 2))  # Method 1
print("The value of pi is:", format(pi, ".2f"))  # Method 2
print("The value of pi is:", f"{pi:.2f}")  # Method 3
print("The value of pi is:", "{:.2f}".format(pi))  # Method 4
print("The value of pi is:", "%.2f" % pi)  # Method 5
print("The value of pi is:", str(round(pi, 2)))  # Method 6

# +=, -=, *=, /=, //=, %=, **=
a = 10
b = 3

a += b  # Add and assign
print("a += b:", a)

a -= b  # Subtract and assign
print("a -= b:", a)

a *= b  # Multiply and assign
print("a *= b:", a)

a /= b  # Divide and assign
print("a /= b:", a)

a //= b  # Floor divide and assign
print("a //= b:", a)

a %= b  # Modulus and assign
print("a %= b:", a)

a **= b  # Exponentiate and assign
print("a **= b:", a)

# f-strings examples
name = "Alice"
age = 30
height = 5.7
weight = 150.5
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height} ft, Weight: {weight} lbs, Student: {is_student}")