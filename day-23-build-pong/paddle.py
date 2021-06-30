from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.position)

    def paddle_move_up(self):
        new_y = self.ycor() + 20
        self.goto((self.xcor(), new_y))

    def paddle_move_down(self):
        new_y = self.ycor() - 20
        self.goto((self.xcor(), new_y))
