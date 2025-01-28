from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear()
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Score:{self.score} ", align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align='center', font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()