from turtle import Turtle, Screen

# Constants for movement
MOVE_DISTANCE = 10
TURN_ANGLE = 10


def display_title():
    """Display the program title."""
    print("Welcome to the Etch-A-Sketch Program!")


def setup_key_bindings(screen: Screen, turtle_instance: Turtle):
    """Set up key bindings for controlling the turtle."""

    def move_forward(turtle_instance: Turtle):
        """Move the turtle forward."""
        turtle_instance.forward(MOVE_DISTANCE)

    def move_backward(turtle_instance: Turtle):
        """Move the turtle backward."""
        turtle_instance.backward(MOVE_DISTANCE)

    def turn_left(turtle_instance: Turtle):
        """Turn the turtle left."""
        turtle_instance.left(TURN_ANGLE)

    def turn_right(turtle_instance: Turtle):
        """Turn the turtle right."""
        turtle_instance.right(TURN_ANGLE)

    def clear_screen():
        """Clear the screen and reset the turtle to blue with a blue line."""
        screen.reset()
        turtle_instance.color("blue")
        turtle_instance.shape("turtle")

    def exit_program():
        """Exit the program."""
        screen.bye()

    # Listen for key presses
    screen.listen()
    # Bind keys to actions
    screen.onkey(lambda: move_forward(turtle_instance), "Up")  # Move forward
    screen.onkey(lambda: move_backward(turtle_instance), "Down")  # Move backward
    screen.onkey(lambda: turn_left(turtle_instance), "Left")  # Turn left
    screen.onkey(lambda: turn_right(turtle_instance), "Right")  # Turn right
    screen.onkey(clear_screen, "C")  # Clear screen
    screen.onkey(clear_screen, "c")  # Clear screen
    screen.onkey(exit_program, "Q")  # Exit program
    screen.onkey(exit_program, "q")  # Exit program


def main():
    """Main function to set up the turtle and screen."""
    display_title()
    screen = Screen()
    turtle_instance = Turtle()

    # Example: Set up the turtle
    turtle_instance.shape("turtle")
    turtle_instance.color("blue")

    # Set up key bindings
    setup_key_bindings(screen, turtle_instance)

    # Keep the screen open until clicked
    screen.mainloop()


if __name__ == "__main__":
    main()
