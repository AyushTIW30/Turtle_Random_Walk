import turtle as t
import random

# Setup screen
screen = t.Screen()
screen.bgcolor("#1e1e1e")  # Dark modern background
screen.title("Glowing Turtle Walk")

# Setup turtle
tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.pensize(10)
tim.speed("fastest")
tim.penup()
tim.goto(0, 0)
tim.pendown()

# Movement directions
directions = [0, 90, 180, 270]

# Function to generate glowing random colors
def random_color():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    return (r, g, b)

# Make a glowing random walk
for _ in range(300):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(directions))

# Exit on click
screen.exitonclick()
