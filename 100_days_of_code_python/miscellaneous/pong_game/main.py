from turtle import Turtle
from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")




pad = Paddle()

screen.exitonclick()