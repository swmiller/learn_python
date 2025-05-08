from turtle import Turtle, Screen
import random


def setup_screen():
    """Set up the game screen with a black background and a title."""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    return screen


def create_snake_body(length):
    """Initialize the snake body with a specified length.

    Args:
        length (int): The number of segments in the snake body.

    Returns:
        list: A list of Turtle objects representing the snake body.
    """
    segments = []
    start_x = 0  # Starting x-coordinate for the snake head

    for _ in range(length):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(start_x, 0)  # Position each segment horizontally
        segments.append(segment)
        start_x -= 20  # Move the next segment 20 pixels to the left

    return segments


def draw_snake(snake_segments):
    """Display the snake on the screen by showing its segments.

    Args:
        snake_segments (list): A list of Turtle objects representing the snake body.
    """
    for segment in snake_segments:
        segment.showturtle()


def move_snake_body(segments):
    """Move the snake body forward by one Turtle size.

    Args:
        segments (list): A list of Turtle objects representing the snake body.
    """
    for i in range(start=(len(segments) - 1), stop=0, step=-1):
        # Move each segment to the position of the segment in front of it
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)

    # Move the head forward
    segments[0].forward(20)


def main():
    """Main function to run the snake game."""
    print("Welcome to the Snake Game!")
    # Initialize the game
    screen = setup_screen()

    # Add your game logic here
    snake_segments = create_snake_body(3)
    draw_snake(snake_segments)

    for _ in range(10):
        move_snake_body(snake_segments)
        screen.update()

    # Keep the window open until closed by the user
    screen.mainloop()


if __name__ == "__main__":
    main()
