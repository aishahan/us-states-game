import turtle
from turtle import Screen, Turtle
import pandas
import states


screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
map = Turtle()
screen.addshape(image)
map.shape(image)


state_count = 0
guessed_list = []
answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name?").title()
print(answer_state)


game_is_on = True
while game_is_on:
    if answer_state == "Exit":
        missing_states = [x for x in states.list if x not in guessed_list]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in states.list:
        if answer_state in guessed_list:
            pass
        else:
            guessed_list.append(answer_state)
            state_count += 1
            new_state = Turtle()
            new_state.hideturtle()
            new_state.penup() 
            state_data = states.data[states.data.state == answer_state]
            new_state.goto(int(state_data.x), int(state_data.y))            
            new_state.write(answer_state)
    answer_state = screen.textinput(title=f"{state_count}/50 States Guessed",prompt="What's another state's name?").title()
    print(answer_state)
    if state_count == 50:
        game_is_on = False
    


screen.exitonclick()

