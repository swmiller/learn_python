# Reading a file line by line using the 'with' statement
file_path = "data.txt"

try:
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())  # Use strip() to remove any trailing newline or whitespace
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
