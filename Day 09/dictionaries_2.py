import json

# Nested Dictionary Example
# Creating a dictionary with a list as a value
nested_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "broccoli", "spinach"],
    "grains": ["rice", "wheat", "oats"],
}

print(json.dumps(nested_dict, indent=4))


# Print type of nested_dict
print()
print(f"Type: nested_dict = {type(nested_dict)}")

# Print type of fruits in nested_dict
print(f"Type: fruits      = {type(nested_dict["fruits"])}")

# Print type of first element in fruits
print(f"Type: fruits[0]   = {type(nested_dict['fruits'][0])}")

# Print the first element with the "fruits" key
print(f"First element: fruits[0] = {nested_dict['fruits'][0]}")

# Create a nested list using aplhabet letter A to D
nested_list = ["A", "B", ["C", "D"]]
print(f"Print 'C': {nested_list[2][0]}")

# Create a dictionary within a dictionary: Key = Country with nexted City dictionary and fake population
population = {
    "USA": {
        "New York": 8419600,
        "Los Angeles": 3980400,
        "Chicago": 2716000,
    },
    "Canada": {
        "Toronto": 2731571,
        "Vancouver": 631486,
        "Montreal": 1780000,
    },
    "Mexico": {
        "Mexico City": 8918653,
        "Guadalajara": 5295912,
        "Monterrey": 4423000,
    },
}

print(json.dumps(population, indent=4))

# Print Toronto, Canada population
print(f"Toronto, Canada population: {population['Canada']['Toronto']}")

# Print the structure of the "population" dictionary
for country, cities in population.items():
    print(f"Country: {country}")
    for city, pop in cities.items():
        print(f"  City: {city}, Population: {pop}")
