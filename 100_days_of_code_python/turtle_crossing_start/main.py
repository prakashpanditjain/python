import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(my_player.move_forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.generate_car()
    car_manager.move_car()

    #detect collision of turtle with car_manager
    for car in car_manager.all_car:
        if my_player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y)./
    if my_player.is_at_finish_line():
        my_player.go_to_start()
        score_board.level_up()




screen.exitonclick()