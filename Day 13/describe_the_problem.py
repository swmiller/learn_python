def my_function():
    for i in range(
        1, 21
    ):  # Change to 21 so that the "You got it" message can be printed
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#    The loop is counting from 1 to 19
# 2. When is the function meant to print "You got it"?
#    The function will print "You got it" when the value of i is 20. However, that will never happen because the loop only goes up to 19.
# 3. What are your assumptions about the value of i?
#    I suppose the value of i was supposed to go up to 20, but the loop is currently set to go only up to 19.
