import random
import turtle
from platform import win32_is_iot
from turtle import Screen
from turtle import Turtle

from numpy.lib.type_check import isreal

is_race_on = False
screen = Screen()
screen.setup(width=500,height=500)
user_bets = screen.textinput(title="make your bet!",prompt="Which turtle will win the race? Enter a color: ")
colors = ['red','green','black','blue','pink','orange']
y_axis = -150
all_turtle =[]

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_axis)
    y_axis += 50
    all_turtle.append(new_turtle)

if user_bets:
    is_race_on = True

print(all_turtle)

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            winnig_turtle = turtle.pencolor()
            if winnig_turtle == user_bets:
                print("You have won!! cheers !!!")
            else:
                print("you have lose..better luch next time")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
