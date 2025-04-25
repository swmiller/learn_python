from person import Person

# Example of working with the Person class
if __name__ == "__main__":
    # Creating a Person object
    person1 = Person("John", "Doe", 30)

    # Accessing properties using getters
    print(f"Firstname: {person1.firstname}")
    print(f"Lastname: {person1.lastname}")
    print(f"Age: {person1.age}")

    # Modifying properties using setters
    person1.firstname = "Jane"
    person1.lastname = "Smith"
    person1.age = 40

    # Accessing updated properties
    print("\nUpdated Person Details:")
    print(f"Firstname: {person1.firstname}")
    print(f"Lastname: {person1.lastname}")
    print(f"Age: {person1.age}")

    # Attempting to set invalid age
    try:
        person1.age = -5
    except ValueError as e:
        print(f"Error: {e}")

    try:
        person1.age = 130
    except ValueError as e:
        print(f"Error: {e}")
