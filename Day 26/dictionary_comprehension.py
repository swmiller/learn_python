import pprint
import random

states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
]

# Create a dictionary with state names as keys and their lengths as values
state_random = {state: random.randint(1, 100) for state in states}

# Print the dictionary
print("Original dictionary:")
pprint.pprint(state_random)

# Create a new dictionary from the existing one, filtering out states with lengths less than or equal to 50
filtered_state_random = {
    state: length for state, length in state_random.items() if length <= 50
}

# Print the filtered dictionary
print("\nFiltered dictionary (length <= 50):")
pprint.pprint(filtered_state_random)
