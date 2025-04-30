from turtle import Turtle, Screen
import colorsys


def mandelbrot_iteration(c, max_iter):
    """
    Determine if a complex number c is in the Mandelbrot set.
    Returns the number of iterations before the value escapes, or max_iter if it's in the set.
    """
    z = 0
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:  # If z escapes the radius 2 circle, c is not in the set
            return i
    return max_iter  # If we reach max_iter, c is likely in the set


def get_color(iterations, max_iter):
    """
    Map the number of iterations to a color.
    """
    if iterations == max_iter:
        return (0, 0, 0)  # Black for points in the set

    # Use HSV color model for smooth coloring
    h = iterations / max_iter
    # Adjust saturation and value for better visual appeal
    s = 0.8
    v = 1.0 if iterations < max_iter else 0

    # Convert HSV to RGB
    rgb = colorsys.hsv_to_rgb(h, s, v)
    # Scale to 0-255 range
    return tuple(int(255 * c) for c in rgb)


def draw_mandelbrot(
    t, screen, width, height, max_iter=100, zoom=1.0, center_x=-0.5, center_y=0
):
    """
    Draw the Mandelbrot set using a Turtle.
    """
    # Setup the screen for pixel-by-pixel drawing
    screen.tracer(0)
    t.hideturtle()
    t.speed(0)

    # Calculate the range of complex coordinates
    min_x = center_x - 2.0 / zoom
    max_x = center_x + 1.0 / zoom
    min_y = center_y - 1.5 / zoom
    max_y = center_y + 1.5 / zoom

    # Size of each pixel in complex plane
    dx = (max_x - min_x) / width
    dy = (max_y - min_y) / height

    # Start drawing from the top-left corner
    for y in range(height):
        t.penup()
        t.goto(-width / 2, height / 2 - y)

        for x in range(width):
            # Map pixel coordinates to complex plane
            c = complex(min_x + x * dx, max_y - y * dy)

            # Calculate iterations for this point
            iterations = mandelbrot_iteration(c, max_iter)

            # Set color based on iterations
            rgb = get_color(iterations, max_iter)
            t.pencolor(rgb[0], rgb[1], rgb[2])  # Use integers directly

            # Draw a single point
            t.pendown()
            t.forward(1)

        # Update the screen every few rows to show progress
        if y % 10 == 0:
            screen.update()

    # Final update
    screen.update()


def main():
    # Setup
    screen = Screen()
    screen.setup(800, 600)
    screen.title("Mandelbrot Set")
    screen.colormode(255)  # Use 0-255 RGB values

    # Create turtle
    t = Turtle()
    t.hideturtle()

    # Draw Mandelbrot
    print("Drawing Mandelbrot set... this may take a while.")
    draw_mandelbrot(t, screen, 800, 600, max_iter=50, zoom=0.6)
    print("Mandelbrot set complete!")

    # Keep the window open until clicked
    screen.exitonclick()


if __name__ == "__main__":
    main()
