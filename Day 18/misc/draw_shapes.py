from turtle import Turtle, Screen
from random import choice

shapes_sides = {
    "square": 4,
    "triangle": 3,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10,
}


def draw_shape(turtle, sides, used_colors):
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "aqua", "pink", "brown", "gray"]
    available_colors = [color for color in colors if color not in used_colors]
    if not available_colors:
        print("No more unique colors available.")
        return

    chosen_color = choice(available_colors)
    used_colors.add(chosen_color)
    turtle.color(chosen_color)  # Set a unique color for the shape

    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)


def move_to_center(turtle):
    # Move turtle to the center of the screen
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def main():
    print("Draw Shapes")
    screen = Screen()
    t = Turtle()
    used_colors = set()

    move_to_center(t)  # Move turtle to the center of the screen

    for shape, sides in shapes_sides.items():
        print(f"Drawing a {shape}...")
        draw_shape(t, sides, used_colors)
        move_to_center(t)  # Reset turtle to the center for the next shape

    screen.mainloop()  # Keep the window open until closed


if __name__ == "__main__":
    main()
