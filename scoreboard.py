from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")

s = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1

    def show_level(self):
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        self.write("GAME OVER", align="right", font=FONT)

    def next_level(self):
        self.level += 1

    def win(self):
        self.write("YOU WIN!!!", align="right", font=("Courier", 72, "normal"))


