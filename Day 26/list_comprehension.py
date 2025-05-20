numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n **2 for n in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)

file1_data = []
with open('data\\file1.txt') as file1:
    file1_data = [int(line.strip()) for line in file1]
print(file1_data)

file2_data = []
with open('data\\file2.txt') as file2:
    file2_data = [int(line.strip()) for line in file2]
print(file2_data)

result = [n for n in file1_data if n in file2_data]
print(result)
