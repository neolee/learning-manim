# use turtle lib to draw a logarithmic spiral
import turtle
import math

# set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# create a turtle named "spiral"
spiral = turtle.Turtle()
spiral.speed(0)
spiral.color("white")

# parameters for the logarithmic spiral
a = 5        # starting radius
b = 0.1      # growth factor

# draw the logarithmic spiral
for i in range(250):
    angle = i * 4          # incremental angle in degrees
    radian = math.radians(angle)  # convert angle to radians
    x = a * math.exp(b * radian) * math.cos(radian)
    y = a * math.exp(b * radian) * math.sin(radian)
    spiral.goto(x, y)

# hide the turtle and display the window
spiral.hideturtle()
screen.mainloop()