height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight / (height ** 2))

# Print the bmi with 2 decimal places.
print(f"{bmi:.2f}")     # Method 1 
print(round(bmi, 2))    # Method 2 (watch out for banker's rounding)

