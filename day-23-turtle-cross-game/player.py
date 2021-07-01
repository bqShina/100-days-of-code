from turtle import Turtle

STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POINT)

    def player_move(self):
        self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.goto(STARTING_POINT)
