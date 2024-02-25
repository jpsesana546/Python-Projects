from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.write(f"Score = {self.score}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)
