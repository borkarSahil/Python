from turtle import Turtle, Screen

the_turtle = Turtle()

#  SQUARE  START
the_turtle.shape("turtle")
the_turtle.color("red")

for _ in range(4):
    the_turtle.forward(100)
    the_turtle.right(90)

#  END


screen = Screen()
screen.exitonclick()
