import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "orange", "black", "green", "blue", "purple"]
pos = [-125, -75, -25, 25, 75, 125]
turtles = []

screen = Screen()

#
# def move_forwards():
#     dan.forward(10)
#
#
# def move_backwards():
#     dan.backward(10)
#
#
# def turn_left():
#     dan.left(10)
#
#
# def turn_right():
#     dan.right(10)
#
#
# def reset():
#     dan.clear()
#     dan.penup()
#     dan.home()
#     dan.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards, "Up")
# screen.onkey(move_backwards, "Down")
# screen.onkey(turn_left, "Left")
# screen.onkey(turn_right, "Right")
# screen.onkey(reset, "Delete")
is_race_done = False
screen.setup(width=800, height=700)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ").lower()

for turtle_index in range(6):
    john = Turtle(shape="turtle")
    john.penup()
    john.color(colors[turtle_index])
    john.goto(-390, pos[turtle_index])
    turtles.append(john)

while not is_race_done:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 390:
            color = turtle.pencolor()
            if color == bet:
                print("You won! Your turtle is the winner!")
            else:
                print(f"You lose! The {color} is the winner!")
            is_race_done = True
screen.exitonclick()
