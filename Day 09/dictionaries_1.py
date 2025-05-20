import pprint

# Nested Dictionary Example
sku = {
    "abc123": {
        "name": "Widget A",
        "price": 19.99,
    },
    "def456": {
        "name": "Widget B",
        "price": 29.99,
    },
    "ghi789": {
        "name": "Widget C",
        "price": 39.99,
    },
}

# Printing the entire dictionary
print("Original SKU Dictionary:")
print(sku)

# Accessing a specific item in the dictionary
print("\nAccessing a specific item:")
print(sku["abc123"])

# Pretty printing the dictionary
print("\nPretty printing the dictionary:")
pprint.pprint(sku)

# Adding a new item to the dictionary
sku["jkl012"] = {
    "name": "Widget D",
    "price": 49.99,
}
print("\nAfter adding a new item:")
pprint.pprint(sku)

# Updating an existing item in the dictionary
sku["abc123"]["price"] = 24.99
print("\nAfter updating an item:")
pprint.pprint(sku)

# Deleting an item from the dictionary
del sku["def456"]
print("\nAfter deleting an item:")
pprint.pprint(sku)

# Iterating through the dictionary
print("\nIterating through the dictionary:")
for key, value in sku.items():
    print(f"SKU: {key}, Details: {value}")

# Checking if a key exists in the dictionary
print("\nChecking if a key exists:")
key_to_check = "ghi789"
if key_to_check in sku:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")
