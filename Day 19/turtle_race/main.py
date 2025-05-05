from turtle import Turtle, Screen, Terminator
import random
from tkinter import simpledialog, Tk
import time

color_list = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]


def get_user_prediction(screen):
    """Ask the user to predict which color turtle will win."""
    user_prediction = screen.textinput(
        title="Predict the Winner",
        prompt="Which color turtle do you think will win? Choose a number:\n1: red\n2: blue\n3: green\n4: yellow\n5: orange\n6: purple\n7: pink",
    )
    try:
        choice = int(user_prediction)
        if 1 <= choice <= len(color_list):
            return color_list[choice - 1]
        else:
            screen.textinput(
                title="Invalid Choice",
                prompt=f"Please enter a number between 1 and {len(color_list)}.",
            )
            return get_user_prediction(screen)
    except ValueError:
        screen.textinput(
            title="Invalid Input", prompt="Invalid input. Please enter a valid number."
        )
        return get_user_prediction(screen)


def get_unique_color(used_colors=set()):
    """Return a unique color from a predefined list of color names."""

    for color in color_list:
        if color not in used_colors:
            used_colors.add(color)
            return color
    raise ValueError("No more unique colors available.")


def display_winner_message(screen, user_prediction, winning_color):
    """Display the race results in the lower left corner of the screen."""
    message = (
        f"Your prediction: {user_prediction}\n"
        f"Winning turtle color: {winning_color}\n"
        f"{'Congratulations! You predicted the winner correctly!' if user_prediction == winning_color else 'Sorry, your prediction was incorrect. Better luck next time!'}"
    )
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(-350, -180)  # Move to the lower left corner
    result_turtle.write(message, align="left", font=("Arial", 12, "normal"))


# Define a constant for the number of contestants
NUMBER_OF_CONTESTANTS = 7  # Default number of contestants


def main():
    """Main entry point of the program."""

    turtles = []

    screen = Screen()
    screen.colormode(255)  # Set color mode to accept RGB tuples

    # Ask the user for their predition of the winning turtle color
    user_prediction = get_user_prediction(screen)

    # Create turtles for each contestant
    for i in range(NUMBER_OF_CONTESTANTS):
        turtle_instance = Turtle()
        turtle_instance.color(
            get_unique_color()
        )  # Assign a unique color to each turtle
        turtle_instance.shape("turtle")
        turtles.append(turtle_instance)

    screen.setup(width=800, height=400)
    screen.bgcolor("white")
    screen.title("Turtle Race Game")
    screen.tracer(0)

    # Calculate vertical spacing and starting position
    spacing = 400 // (NUMBER_OF_CONTESTANTS + 1)
    start_y = -(200 - spacing)

    for index, turtle_instance in enumerate(turtles):
        turtle_instance.penup()
        turtle_instance.goto(
            x=-360, y=start_y + index * spacing
        )  # Adjusted x position for less left spacing

    # Draw a checkered finish line on the right-hand side
    finish_line_x = 360  # X-coordinate for the finish line
    finish_line_y_start = 200  # Top of the screen
    finish_line_y_end = -200  # Bottom of the screen
    square_size = 20  # Size of each square in the checkered pattern

    for y in range(finish_line_y_start, finish_line_y_end, -square_size):
        for offset in (0, square_size):
            turtle_instance = Turtle()
            turtle_instance.hideturtle()
            turtle_instance.penup()
            turtle_instance.shape("square")
            turtle_instance.shapesize(
                stretch_wid=square_size / 20, stretch_len=square_size / 20
            )
            turtle_instance.color(
                "black"
                if (y // square_size) % 2 == (offset // square_size) % 2
                else "white"
            )
            turtle_instance.goto(finish_line_x + offset, y)
            turtle_instance.stamp()

    screen.update()

    winning_color = ""  # Initialize winning color
    try:
        # Start the race
        race_in_progress = True
        while race_in_progress:
            for turtle_instance in turtles:
                random_movement = random.randint(1, 10)  # Generate random movement
                turtle_instance.forward(random_movement)  # Move the turtle forward

                # Check if the turtle has crossed the finish line
                if turtle_instance.xcor() >= finish_line_x:
                    winning_color = turtle_instance.color()[
                        0
                    ]  # Get the color of the winning turtle
                    print(f"The winner is the turtle with color: {winning_color}")

                    # Flash the winning turtle a few times
                    for _ in range(5):
                        turtle_instance.hideturtle()
                        screen.update()
                        time.sleep(0.2)
                        turtle_instance.showturtle()
                        screen.update()
                        time.sleep(0.2)

                    race_in_progress = False  # Exit the race loop

            time.sleep(0.1)  # Add a small delay for smoother animation
            screen.update()

    except Exception as e:
        print(f"An error occurred: {e}")

    # screen.textinput(
    #     title="Race Results",
    #     prompt=(
    #         f"Your prediction: {user_prediction}\n"
    #         f"Winning turtle color: {winning_color}\n"
    #         f"{'Congratulations! You predicted the winner correctly!' if user_prediction == winning_color else 'Sorry, your prediction was incorrect. Better luck next time!'}"
    #     ),
    # )

    display_winner_message(screen, user_prediction, winning_color)

    # Keep screen open and handle termination gracefully
    try:
        screen.mainloop()
    except Terminator:  # Updated to use the correct exception class
        print("The turtle graphics window was closed.")


if __name__ == "__main__":
    main()
