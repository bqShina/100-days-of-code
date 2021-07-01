from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

SCORE_POSITION = (-280, 260)

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.player_move, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.random_cars()
    car_manager.move_car()
    # player hit the car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # finish one level
    if player.ycor() > 280:
        scoreboard.update_score()
        player.go_back()
        car_manager.add_speed()



screen.exitonclick()
