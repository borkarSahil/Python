from turtle import Turtle,Screen
import random
screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed(0)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

# tim.pensize(2)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        change_heading = current_heading + size_of_gap
        tim.setheading(change_heading)

draw_spirograph(5)





screen.exitonclick()
