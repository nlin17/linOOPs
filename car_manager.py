from turtle import Turtle
# from main import teddy
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = 1/3

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(300, (random.randint(-25, 25) * 10))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            # new_x = car.xcor() - (random.randint(1, 4)/10)
            # car.goto(new_x, car.ycor())

    def next_level(self):
        self.speed *= 1.05

    def clear_turtles(self):
        for car in self.cars:
            if car.xcor() <= -310:
                car.goto(310, car.ycor())






