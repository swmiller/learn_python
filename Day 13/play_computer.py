year = int(input("What's your year of birth? "))

# The "elif" needs to be >= 1994, not > 1994
if year > 1980 and year < 1994:
    print("You are a millennial.")
# elif year > 1994:
elif year >= 1994:
    print("You are a Gen Z.")
