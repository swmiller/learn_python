from turtle import Turtle, Screen
import random
from math import cos, sin, radians

# Constants
WALK_LENGTH = 25  # Length of each step in the random walk


def change_pen_color_to_random(turtle):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.pencolor((r, g, b))


def get_random_angle():
    return random.choice([0, 90, 180, 270])


def two_dimensional_random_walk(turtle, steps):
    screen_width = Screen().window_width() // 2
    screen_height = Screen().window_height() // 2

    for _ in range(steps):
        change_pen_color_to_random(turtle)
        angle = get_random_angle()
        turtle.setheading(angle)

        # Convert angle to radians for trigonometric calculations
        angle_in_radians = radians(angle)

        # Calculate the next position
        next_x = turtle.xcor() + WALK_LENGTH * cos(angle_in_radians)
        next_y = turtle.ycor() + WALK_LENGTH * sin(angle_in_radians)

        # Check if the next position is within bounds
        if (
            -screen_width < next_x < screen_width
            and -screen_height < next_y < screen_height
        ):
            turtle.forward(WALK_LENGTH)
        else:
            # Redirect the turtle back into the screen
            turtle.setheading((angle + 180) % 360)


def main():
    screen = Screen()
    screen.colormode(255)  # Enable RGB color mode

    turtle = Turtle()
    turtle.pensize(15)  # Set pen size for better visibility
    turtle.speed(0)  # Set the fastest speed

    two_dimensional_random_walk(turtle, 1000)

    screen.mainloop()


if __name__ == "__main__":
    main()
