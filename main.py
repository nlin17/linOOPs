import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

teddy = Player()
teddy.penup()
teddy.setheading(90)
teddy.goto(0, -280)

ben = CarManager()
ben.color("white")
ben.goto(-1000,0)

sb = Scoreboard()
sb.penup()
sb.goto(-220, 250)


screen.onkey(teddy.u, "Up")
screen.onkey(teddy.d, "Down")
screen.onkey(teddy.l, "Left")
screen.onkey(teddy.r, "Right")

screen.listen()

global i
i = 105

on = True

while on:
    # time.sleep(0.1)
    sb.show_level()
    screen.update()
    x = random.randint(0, i)
    if x == 1:
        ben.create_car()

    for car in ben.cars:
        if teddy.distance(car.xcor(), car.ycor()) <= 20:
            sb.game_over()
            on = False


    ben.move()
    ben.clear_turtles()

    if teddy.ycor() >= 250:
        sb.clear()
        ben.clear()
        # i -= 10
        ben.speed += 1/3
        teddy.goto(0, -280)
        sb.next_level()


    if sb.level == 10:
        sb.goto(0, 0)
        screen.clear()
        sb.clear()
        sb.win()








