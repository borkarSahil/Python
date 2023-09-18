from turtle import Turtle

STARTING_POSITION = [(-350, 0), (350, 0)]

class Paddle:
     def __init__(self):
         self.paddles = []
         self.create_paddle()
         self.paddle1 = self.paddles[0]
         self.paddle2 = self.paddles[1]

     def create_paddle(self):
         for position in STARTING_POSITION:
             new_paddle = Turtle()
             new_paddle.shape("square")
             new_paddle.color("white")
             new_paddle.penup()
             new_paddle.speed(0)
             new_paddle.shapesize(stretch_wid=5, stretch_len=1)
             new_paddle.goto(position)
             self.paddles.append(new_paddle)

     def move_Up(self):
         y_position = self.paddles[0].ycor() + 50
         self.paddle1.goto(x=350, y=y_position)

     def move_Down(self):
         y_position = self.paddles[0].ycor() - 50
         self.paddle1.goto(x=350, y=y_position)

