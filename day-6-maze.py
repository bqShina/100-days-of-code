def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn():
    turn_right()
    move()
    

while not at_goal(): 

    if front_is_clear():
        if wall_on_right():
            move()
        elif right_is_clear():
            turn()
    elif wall_in_front():
        if right_is_clear():
            turn()           
        elif wall_on_right():
            turn_left()
