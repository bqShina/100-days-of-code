import turtle
import pandas
from state_text import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_column = data["state"]
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        state_missed = []
        for state in state_column:
            if state not in guessed_state:
                state_missed.append(state)
        state_missed_data = pandas.DataFrame(state_missed)
        state_missed_data.to_csv("states_to_learn.csv")
        break
    for state in state_column:
        if answer_state == state:
            guessed_state.append(answer_state)
            state_data = data[state_column == state]
            answer = State(answer_state, int(state_data.x), int(state_data.y))



# How to get position of states
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

screen.exitonclick()
