from smtplib import SMTPConnectError
from turtle import Screen
from turtle import Turtle

from geocoder.keys import here_app_id

from fibonacci_number import fibonacci_number

tim = Turtle()
screen = Screen()
tim.color('red')
tim.speed('fastest')

fib = fibonacci_number()
print(fib)
heading = 0
for i in range(len(fib)):
    if fib[i] != 0 :
        if i == 1:
            distance = i *10
            for heading in (90,180,270,0):
                tim.forward(distance)
                tim.setheading(heading)
            tim.forward(distance)
        else:
            for _ in range(4):
                tim.forward(fib[i] * 10)
                if heading > 270:
                    heading = 0
                heading += 90
                tim.setheading(heading)
            tim.forward(fib[i] * 10)
            if heading > 270:
                heading = 0
            heading += 90
            tim.setheading(heading)
            tim.forward(fib[i] * 10)


screen.exitonclick()