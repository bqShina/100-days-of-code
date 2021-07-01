from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scoreboard_1 = Scoreboard((50, 250))
scoreboard_2 = Scoreboard((-50, 250))

line = Line()

screen.listen()
screen.onkey(paddle_1.paddle_move_up, "Up")
screen.onkey(paddle_1.paddle_move_down, "Down")
screen.onkey(paddle_2.paddle_move_up, "w")
screen.onkey(paddle_2.paddle_move_down, "s")
game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    # detect ball hit wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect ball hit paddle_1
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Miss the ball
    if ball.xcor() > 420:
        ball.reset_ball()
        scoreboard_2.update_score()

    elif ball.xcor() < -420:
        ball.reset_ball()
        scoreboard_1.update_score()


screen.exitonclick()
