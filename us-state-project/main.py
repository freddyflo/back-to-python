import pandas
import turtle 
from art import logo

# ASCII art logo
print(logo)


# Screen
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

count = 0
is_game_on = True


def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

# read CSV file
df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()


correct_guesses = []
NO_OF_STATES = 50



while is_game_on:
    answer = screen.textinput(title=f"{count}/50 States Correct", prompt="What's another state's name?").title()

    if answer == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        missing_states = [ state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)     
        new_data.to_csv("states_to_learn.csv")
        break
    answer_state = answer.capitalize()
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        df[df.state == answer_state]
        state_info = df[df.state == answer_state]
        x_coordinate = int(state_info["x"])
        y_coordinate = int(state_info["y"])
        t.goto(x_coordinate, y_coordinate)
        t.write(answer_state, True, align="center")
        correct_guesses.append(answer_state)
        count += 1
    if len(correct_guesses) == NO_OF_STATES:
        is_game_on = False

