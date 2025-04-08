import random

# Simulate a coin flip by generating a random float between 0.0 and 1.0
coin_flip_value = random.random()
print(f"Generated random value: {coin_flip_value}")

# Determine the result of the coin flip
if coin_flip_value > 0.5:
    print("Result: Heads")
else:
    print("Result: Tails")
