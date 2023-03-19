# import colorgram

colors = [(37, 172, 104), (237, 113, 205), (229, 82, 152), (119, 39, 91), (184, 77, 49), (233, 144, 115),
          (112, 184, 104), (64, 110, 170), (214, 85, 65), (198, 36, 15), (129, 216, 179), (121, 140, 192),
          (228, 42, 65), (129, 36, 177), (22, 124, 60), (21, 104, 137), (155, 194, 222), (35, 79, 40), (80, 35, 30),
          (182, 220, 168), (28, 166, 160), (164, 29, 31), (232, 181, 167), (68, 34, 42), (73, 45, 77), (238, 160, 171)]
# colors = colorgram.extract('hirst_painting.jpg', 30)
# rgb_colors =[]
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.b, color.rgb.g)
#     rgb_colors.append(new_color)
# print(rgb_colors)

from turtle import Turtle, Screen
import random

turtle.colormode(255)
dan = Turtle()
dan.penup()
# dan.setheading(225)
# dan.forward(300)
# dan.setheading(0)
# for i in range(10):
#     for _ in range(10):
#         dan.dot(20, random.choice(colors))
#         dan.forward(50)
#     dan.setheading(90)
#     dan.forward(50)
#     if i%2 == 0:
#         dan.setheading(180)
#         dan.forward(50)
#     else:
#         dan.setheading(0)
#         dan.forward(50)

for i in range(100):
    dan.forward(40+i/2)
    dan.right(54 -(i/4))
    dan.dot(10 + i/5, random.choice(colors))

turtle.done()
screen = Screen()
screen.exitonclick()
