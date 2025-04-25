class Person:
    def __init__(self, firstname, lastname, age):
        # Constructor to initialize Person attributes
        self.firstname = firstname
        self.lastname = lastname
        self._age = None  # Use a private attribute for age
        self.age = age  # Use the setter to validate age

    @property
    def firstname(self):
        # Getter for firstname
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        # Setter for firstname
        if not value:
            raise ValueError("Firstname cannot be empty.")
        self._firstname = value

    @property
    def lastname(self):
        # Getter for lastname
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        # Setter for lastname
        if not value:
            raise ValueError("Lastname cannot be empty.")
        self._lastname = value

    @property
    def age(self):
        # Getter for age
        return self._age

    @age.setter
    def age(self, value):
        # Setter for age
        if not isinstance(value, (int, float)):
            raise ValueError("Age must be a numeric value.")
        if value < 0 or value > 125:
            raise ValueError("Age must be between 0 and 125.")
        self._age = value