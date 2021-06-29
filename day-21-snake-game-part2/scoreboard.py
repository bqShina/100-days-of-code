from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.score_detect()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def score_detect(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
