# TODO : Border and middle line
# TODO : Score Card
# TODO : 2 Turtle which will move
# TODO : 1 ball

# TODO : CREATE THE SCREEN
# TODO : CREATE AND MOVE A PADDLE
# TODO : CREATE ANOTHER PADDLE
# TODO : CREATE THE BALL AND MAKE IT MOVE
# TODO : DETECT COLLISION WITH WALL AND BOUNCE
# TODO : DETECT COLLISION WITH PADDLE
# TODO : DETECT WHEN PADDLE MISSES
# TODO : KEEP SCORE

from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)
screen.title("Pong")
screen.tracer(0)

# Paddle
paddle = Paddle()

screen.listen()

screen.onkey(key="Up", fun=paddle.move_Up)
screen.onkey(key="Down", fun=paddle.move_Down)


screen.exitonclick()