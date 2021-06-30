from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -300)
        self.make_line()

    def make_line(self):
        self.setheading(90)
        for n in range(30):
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()
