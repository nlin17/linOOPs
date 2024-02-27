import random
import turtle
from turtle import Screen
teddy = turtle.Turtle()
screen = Screen()
teddy.shape("turtle")
turtle.colormode(255)

directions = [90, 180, 270, 360]
# for i in range(0, 360):
#     directions.append(i)

while True:
    teddy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    teddy.right(random.choice(directions))
    teddy.forward(20)

screen.exitonclick()