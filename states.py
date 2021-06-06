import pandas
import turtle

from turtle import Turtle

data = pandas.read_csv("50_states.csv")



list_of_states = data["state"]
list = []

for state in list_of_states:
    list.append(state)


# def find_coordinates():

#     x = data[data["x"] == answer_state]
#     y = data[data["y"] == answer_state]
#     return (x,y)

#print(find_coordinates())




