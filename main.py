from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 ", prompt="What is another state? ").title()
    missing_states = []

    for state in all_states:
        if state not  in guessed_state:
            missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("State_to_learn.csv")
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        x_coordinate = int(state_data.x)
        y_coordinate = int(state_data.y)
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coordinate, y_coordinate)
        t.write(answer_state, align="center", font=("Arial", 12, "normal"))
