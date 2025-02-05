import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_car =[]
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_int = random.randint(0,6)
        if random_int == 6:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(280, random.randint((-220), 250))
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT