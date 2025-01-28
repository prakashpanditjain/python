import time
from turtle import Turtle
from turtle import  Screen
starting_position = [(0,0), (-20,0), (-40,0)]

class Snake():

    def __init__(self):
        self.segment = []
        self.x_pos = 0
        self.create_snake()
        self.distnace_move = 20
        self.head = self.segment[0]
        self._up = 90
        self._down = 270
        self._right = 0
        self._left = 180

    def up(self):
        if self.head.heading() != self._down:
            self.head.setheading(self._up)

    def down(self):
        if self.head.heading() != self._up:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != self._left:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != self._right:
            self.head.setheading(180)

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position=position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segment.append(snake)

    def extend_snake(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_number in range(len(self.segment)-1, 0 ,-1):
            new_x = self.segment[seg_number -1].xcor()
            new_y = self.segment[seg_number -1].ycor()
            self.segment[seg_number].goto(new_x, new_y)

        self.segment[0].forward(distance=self.distnace_move)

