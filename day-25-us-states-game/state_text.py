from turtle import Turtle

FONT = ("Arial", 14, "normal")
ALIGNMENT = "center"


class State(Turtle):
    def __init__(self, text, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write_text(text)

    def write_text(self, text):
        self.write(arg=text, align=ALIGNMENT, font=FONT)



