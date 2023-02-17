# Instances, State, High Order Functions

import turtle
import random


screen = turtle.Screen()
screen.setup(width=500, height=400)


# *** TURTLE RACE ***
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color(red/orange/yellow/green/blue/purple): ")
colors = [ "red", "orange", "yellow", "green", "blue", "purple" ]
turtles = []
y_axis = -100

for color in range(6):
    new_turle = turtle.Turtle(shape="turtle")
    new_turle.color(colors[color])
    new_turle.penup()
    new_turle.goto(x=-240, y=y_axis)
    y_axis += 40
    turtles.append(new_turle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()