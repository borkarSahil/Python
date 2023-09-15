from turtle import  Turtle,Screen
screen = Screen()
import random

# background = 'racetrack.png'
# screen.bgpic(background)
# screen.screensize(500,800)
is_race_on = False

screen.setup(width=500, height=600)
user_bet = screen.textinput(title="Make a bet", prompt="Enter the color ")

y_post = [-100, -50, 0, 50, 100, 150]
colors = ["red", "blue", "yellow", "green", "black", "grey"]

turtle_list = []
for turtle_index in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.color()
    t.penup()
    t.goto(x= -230, y= y_post[turtle_index])
    turtle_list.append(t)

# print(turtle_list)
if user_bet:
    is_race_on = True

i=0
while is_race_on:
    rand_dist = random.randint(0,15)
    turtle_list[i].forward(rand_dist)
    i += 1

    if i==6:
        i=0

    if turtle_list[i].xcor() >= 150:
        winning_color = turtle_list[i].pencolor()
        if winning_color == user_bet:
            print(winning_color, " You Won")
        else:
            print("Hard Luck !" ,winning_color, "Won")
        is_race_on = False



screen.exitonclick()