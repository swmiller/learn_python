# use alias: from turtle import Turtle as t, Screen as s
from turtle import Turtle, Screen


# Set up the screen
screen = Screen()
screen.title("Turtle Challenge 1")
screen.bgcolor("white")


# Random color function
def random_color():
    import random

    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


# Main function
def main():
    # Create a turtle object
    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.color(random_color())  # Set a random color
    my_turtle.speed(5)

    # Challenge 1: Draw a square
    for _ in range(4):
        my_turtle.forward(100)  # Move forward by 100 units
        my_turtle.right(90)  # Turn right by 90 degrees
        my_turtle.color(random_color())  # Change color after each side

    # Keep the window open until clicked
    screen.mainloop()


if __name__ == "__main__":
    main()
