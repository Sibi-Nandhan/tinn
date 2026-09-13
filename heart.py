import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Set to fastest speed so it draws efficiently
t.hideturtle()
t.penup()
t.color("#ffb6c1")  # Light pink color

# Loop to create the heart layers
for scale in range(11, 17):
    for i in range(120):
        # Calculate the angle for the mathematical heart curve
        angle = (math.pi * 2) / 120 * i
        
        # Parametric equations for a heart shape
        x = 16 * (math.sin(angle) ** 3) * scale
        y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * scale
        
        # Move to the coordinate and write the text
        t.goto(x, y)
        t.write("I love you", align="center", font=("Arial", 8, "bold"))

# Keep the window open
turtle.done()