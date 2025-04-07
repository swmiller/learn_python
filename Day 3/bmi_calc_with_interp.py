# BMI Calculator with Interpretation

# 🚨 Do not modify the values below
weight = 85  # in kilograms
height = 1.85  # in meters

# Calculate BMI
bmi = weight / (height**2)

# Interpret BMI
if bmi < 18.5:
    interpretation = "underweight"
elif 18.5 <= bmi < 25:
    interpretation = "normal weight"
else:
    interpretation = "overweight"

# Print BMI and interpretation
print(f"Your BMI is {bmi:.2f}, you are {interpretation}.")
