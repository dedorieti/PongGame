from turtle import Turtle

DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.score = 0
        if side == "right":
            self.goto(x=350, y=0)
        else:
            self.goto(x=-350, y=0)

    def paddle_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + DISTANCE
            self.goto(x=self.xcor(), y=new_y)

    def paddle_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - DISTANCE
            self.goto(x=self.xcor(), y=new_y)
