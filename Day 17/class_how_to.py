class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # def __init__(self):
    #     pass

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        return f"The {self.get_description()} engine has started."


# Example usage:
if __name__ == "__main__":
    my_car = Car(make="Honda", model="Civic", year=2021)
    print(f"\nDescription: {my_car.get_description()}")  # Output: 2020 Toyota Corolla
    print(
        f"Vroom      : {my_car.start_engine()}"
    )  # Output: The 2020 Toyota Corolla engine has started.

    # Raw print the class
    print()
    print(my_car)  # Output: <__main__.Car object at 0x...>

    # Loop through the class attributes
    print()
    for attr in dir(my_car):
        if not attr.startswith("__"):
            print(f"Attribute: {attr} -> Value: {getattr(my_car, attr)}")
