# Welcome message
print("Welcome to the Tip Calculator!")

# Prompt the user for the total bill amount and convert it to a float
bill_amount = float(input("What was the total bill? $"))

# Prompt the user for the tip percentage and convert it to an integer
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Prompt the user for the number of people to split the bill and convert it to an integer
people = int(input("How many people to split the bill? "))

# Calculate the tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total amount including the tip
total_amount = bill_amount + tip_amount

# Calculate the amount each person should pay
amount_per_person = total_amount / people

# Round the amount to 2 decimal places using round
amount_per_person = round(amount_per_person, 2)

# Format the amount to 2 decimal places for display
formatted_amount_per_person = "{:.2f}".format(amount_per_person)

# Print the amount each person should pay
print(f"Each person should pay: ${formatted_amount_per_person}")
