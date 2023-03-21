from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

paddle_r = Paddle("r")
paddle_l = Paddle("l")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")

screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce("y")

    # paddle
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 450) or (ball.distance(paddle_l) < 50 and ball.xcor() < -450):
        ball.bounce("x")

    # death r
    if ball.xcor() > 500:
        scoreboard.increase_score("l")
        scoreboard.update_score()
        ball.reset_position()
    # death l
    if ball.xcor() < -500:
        scoreboard.increase_score("r")
        scoreboard.update_score()
        ball.reset_position()


screen.exitonclick()
