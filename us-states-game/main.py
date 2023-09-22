import turtle
import pandas
data = pandas.read_csv("./50_states.csv")

screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
# screen.bgpic(image)
screen.addshape(image)
turtle.shape(image)

# If ansState == state present in file
# If it is right
# Create a turtle and goto x,y

# Taking state row and converting it into row
all_states = data["state"].to_list()

guessed_state = []

game_is_on = True
while game_is_on and len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"Score : {len(guessed_state)}/50", prompt="Whats another state")

    if answer_state in all_states:
        guessed_state.append(answer_state)

        state_row = data[data["state"] == answer_state]
        # print(state_row)
        name_turtle = turtle.Turtle()
        name_turtle.hideturtle()
        name_turtle.penup()
        x_cor = int(state_row["x"])
        y_cor = int(state_row["y"])
        name_turtle.goto(x= x_cor, y= y_cor)
        name_turtle.write(answer_state)

    if answer_state == "off":
        game_is_on = False
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missied_state.csv")


    # screen.update()







# screen.exitonclick()


# To get the coordinate of click location
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


turtle.mainloop()