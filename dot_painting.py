import colorgram
import turtle
import random
tree = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()

tree.speed(10000)


colors = colorgram.extract('dot_painting.jpg', 10)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

screen.setup(width=660, height=660)
screen.bgcolor("black")

x_start = -270
y_start = 270
spacing = 60

tree.penup()
for x in range(10):
    for i in range(10):
        tree.color(random.choice(rgb_colors))
        tree.goto(x_start+(spacing*i), y_start-(spacing*x))
        tree.pendown()
        tree.dot(30)
        tree.penup()

screen.exitonclick()