import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed = []


def get_mouse_click_coord(x, y):
    print(x, y)


while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States", prompt="Please enter a state name").title()
    states = data.state.to_list()

    if answer_state == "Close":
        missing = []
        for state in states:
            if state not in guessed:
                missing.append(state)
        new_file = pandas.DataFrame(missing)
        new_file.to_csv("states_to_improve.csv")
        break

    if answer_state in states:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


