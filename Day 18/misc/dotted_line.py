import turtle


def draw_dotted_line(t):
    # Draw a dotted line
    for _ in range(50):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("Turtle Graphics - Dotted Line Example")

    # Position the turtle to the left side of the window
    screen_width = screen.window_width()
    t.penup()
    t.goto(-screen_width // 2 + 20, 0)  # Move to the left edge with some padding
    t.pendown()

    draw_dotted_line(t)

    screen.mainloop()  # Keep the window open until closed


if __name__ == "__main__":
    main()
