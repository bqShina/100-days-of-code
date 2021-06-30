from turtle import Turtle

FONT = ("Arial", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.position = position
        self.color("white")
        self.goto(self.position)
        self.write("0", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=FONT)
