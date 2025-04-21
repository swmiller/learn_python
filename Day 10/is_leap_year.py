def is_leap_year(year):
    """
    Check if a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4;
    - If it is divisible by 100, it must also be divisible by 400.

    :param year: The year to check.
    :return: True if the year is a leap year, False otherwise.
    """

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap_year(2000))
print(is_leap_year(2100))
