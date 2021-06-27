from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
race_on = False
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for n in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(-230, (100 - 30 * n))
    turtles.append(new_turtle)

if user_bet:
    race_on = True
while race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            race_on = False
            turtle_color = turtle.pencolor()
            if user_bet == turtle_color:
                print(f"You've win. The winner is {turtle_color} turtle")
            else:
                print(f"You've lose. The winner is {turtle_color} turtle")

screen.exitonclick()
