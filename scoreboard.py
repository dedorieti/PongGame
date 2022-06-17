from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def write_score(self, score, position):
        self.clear()
        self.goto(position)
        self.write(score, align="center", font=("Courier", 80, "normal"))
