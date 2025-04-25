# Using a class from a module
from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("red", "yellow")
t.begin_fill()

while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break

t.end_fill()
t.screen.exitonclick()  # Wait for a click to close the window
