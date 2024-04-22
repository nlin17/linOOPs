from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")

    def u(self):
        self.setheading(90)
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def d(self):
        self.setheading(270)
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def l(self):
        self.setheading(180)
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def r(self):
        self.setheading(0)
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())
