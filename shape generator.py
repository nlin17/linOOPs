import turtle
from turtle import Screen
tree = turtle.Turtle()
screen = Screen()

sides = int(input("How many sides? "))
length = int(input("How long is each side? "))

for i in range(0, sides):
    tree.forward(length)
    tree.right(360/sides)

screen.exitonclick()

