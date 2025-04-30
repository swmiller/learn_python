from turtle import Turtle, Screen
import random


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(turtle, radius, gap_angle):
    for _ in range(int(360 / gap_angle)):
        turtle.color(generate_random_color())
        turtle.circle(radius)
        turtle.setheading(turtle.heading() + gap_angle)


def initialize():
    screen = Screen()
    screen.colormode(255)  # Enable RGB color mode

    turtle = Turtle()
    turtle.speed(0)  # Set the fastest speed
    turtle.pensize(2)  # Set pen size for better visibility

    return screen, turtle


def main():
    print("Welcome to the Spirograph program!")

    screen, turtle = initialize()
    draw_spirograph(turtle, radius=100, gap_angle=5)

    screen.mainloop()  # Keep the window open until closed by the user


if __name__ == "__main__":
    main()
