from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.score_l, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.score_r, align="center", font=("Courier", 80, "normal"))

    def increase_score(self, side):
        if side == "r":
            self.score_r += 1
        else:
            self.score_l += 1
