# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:  # Check for FizzBuzz first
            print("FizzBuzz")
        elif number % 3 == 0:  # Check for Fizz
            print("Fizz")
        elif number % 5 == 0:  # Check for Buzz
            print("Buzz")
        else:  # For numbers not divisible by 3 or 5
            print(number)


# Test cases
fizz_buzz(15)  # Should print Fizz, Buzz, and FizzBuzz for the appropriate numbers
fizz_buzz(3)   # Should print Fizz for 3
fizz_buzz(5)   # Should print Buzz for 5
fizz_buzz(1)   # Should print 1 for 1