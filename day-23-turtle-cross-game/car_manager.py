from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVING_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVING_DISTANCE

    def random_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(colors))
            car.setheading(180)
            new_y = random.randint(-250, 250)
            car.goto(300, new_y)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def add_speed(self):
        self.move_distance += MOVE_INCREMENT
        print(self.move_distance)

