import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# This way
# who_pays = random.randint(0, len(friends) - 1)
# print(f"{friends[who_pays]} is going to pay the bill today!")

# or this way
print(f"{random.choice(friends)} is going to pay the bill today!")
