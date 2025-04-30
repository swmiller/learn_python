import random
from turtle import Turtle, Screen
from color_pallet import rgp_color_pallet


def choose_color(colors):
    return random.choice(colors)


def draw_painting(turt, colors):
    grid_size = 10
    spacing = 50
    dot_size = 20

    # Calculate the offset to center the grid
    x_offset = -(grid_size * spacing) // 2 + spacing // 2
    y_offset = -(grid_size * spacing) // 2 + spacing // 2

    for y in range(grid_size):
        for x in range(grid_size):
            turt.penup()
            # Adjust the position to include the offset
            turt.goto(x * spacing + x_offset, y * spacing + y_offset)
            turt.pendown()
            turt.dot(dot_size, choose_color(colors))  # Draw a dot with a random color


def main():

    # Initialize turtle
    turt = Turtle()
    turt.speed("fastest")

    screen = turt.screen
    screen.colormode(255)

    grid_size = 10
    spacing = 50
    screen_width = grid_size * spacing
    screen_height = grid_size * spacing
    screen.setup(
        width=screen_width + spacing, height=screen_height + spacing
    )  # Add padding

    screen.title("Hirst Painting")
    screen.bgcolor("white")

    # Requirments
    # 1. Use a 10 by 10 grid.
    # 2. Fill the grid in with spots that are about 20 in size.
    # 3. Each dot should be spaced about 50 paces apart.
    # 4. Use the color palette provided in the hirst/color_pallet.py file.

    draw_painting(turt, rgp_color_pallet)

    # Hide the turtle after drawing
    turt.hideturtle()
    screen.mainloop()  # Keep the window open


if __name__ == "__main__":
    main()
