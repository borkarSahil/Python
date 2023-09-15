# import turtle as t
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

# APPROACH 1

# tim.penup()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
#
# dotNum = 100
# for dot_count in range(1,dotNum+1):
#         tim.dot(20, random_color())
#         tim.fd(50)
#
#         if dot_count % 10 == 0:
#             tim.setheading(90)
#             tim.forward(50)
#             tim.setheading(180)
#             tim.forward(500)
#             tim.setheading(0)


# APPROACH 2
tim.penup()
position_x = -250
position_y = -250
tim.setposition(position_x, position_y)


for _ in range(10):
    tim.setposition(position_x, position_y)
    for _ in range (10):
        tim.dot(20 , random_color())
        tim.forward(50)

    position_y += 50





screen.exitonclick()