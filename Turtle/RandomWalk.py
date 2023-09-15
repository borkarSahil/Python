from turtle import Turtle, Screen
import random
the_turtle = Turtle()

screen = Screen()
screen.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r,g,b)
    return my_tuple

directions = [0, 90, 180, 270]

the_turtle.pensize(8)
the_turtle.speed(0)

for _ in range(150):
    the_turtle.color(random_color())
    the_turtle.forward(50)
    the_turtle.setheading(random.choice(directions))


