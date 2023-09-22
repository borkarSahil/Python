import turtle
# from turtle import Turtle,Screen

screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
# screen.bgpic(image)
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="Whats another state")
print(answer_state)

screen.exitonclick()


# To get the coordinate of click location
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()