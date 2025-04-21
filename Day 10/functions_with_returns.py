# Function with a simple return value
def add_numbers(a, b):
    return a + b


# Function returning a tuple
def get_coordinates():
    x = 10
    y = 20
    return (x, y)


# Function returning a dictionary
def create_person(name, age):
    return {"name": name, "age": age}


# Function returning a list
def generate_even_numbers(limit):
    return [i for i in range(limit) if i % 2 == 0]


# Function returning None
def print_message(message):
    print(message)
    return None


# Function returning a boolean
def is_even(number):
    return number % 2 == 0


# Example usage
if __name__ == "__main__":
    print(add_numbers(5, 7))  # 12
    print(get_coordinates())  # (10, 20)
    print(create_person("Alice", 30))  # {'name': 'Alice', 'age': 30}
    print(generate_even_numbers(10))  # [0, 2, 4, 6, 8]
    print_message("Hello, World!")  # Prints "Hello, World!"
    print(is_even(4))  # True
