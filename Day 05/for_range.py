# range(start, stop, step) - Generates a sequence of numbers but is not inclusive of the stop value.

for i in range(1, 11):
    print(i)

# Using range to create a list of numbers from 1 to 10 with a step of 1
numbers = list(range(1, 11))
print(numbers)

sum_of_numbers = 0
for i in range(1, 101):
    sum_of_numbers += i
print(f"Sum of numbers from 1 to 100 is: {sum_of_numbers}")
