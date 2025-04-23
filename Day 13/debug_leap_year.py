def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:  # was originally 4000. Changed to 400.
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Test cases
print(is_leap(2000))  # True
print(is_leap(1900))  # False
print(is_leap(2004))  # True
print(is_leap(2001))  # False
