from turtle import Screen
from turtle import Turtle

from PIL.ImageChops import screen

tim = Turtle()

screen = Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    tim.right(20)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def circle():
    tim.circle(50)

screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(circle, 'space')
screen.onkey(clear, 'c')

screen.exitonclick()