from random import randint

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]

# Produces an occasional error because 6 is out of range for the dice_images list
# The error occurs when the random number generated is 6, which is out of range for the dice_images list (0-5).
# dice_num = randint(1, 6)

# Fix
dice_num = randint(0, 5)

print(dice_num)
print(dice_images[dice_num])
