from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280,270) 

    def write_score(self):
        self.clear()
        self.write(f"Level:{self.score}",
                   align="Left",
                   font=FONT)