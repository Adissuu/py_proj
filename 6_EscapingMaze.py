while not at_goal():
    while front_is_clear():
        move()
    if wall_in_front() and wall_on_right():
        turn_left()
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
    while wall_in_front():
        turn_left()
        turn_left()
        turn_left()
    move()
