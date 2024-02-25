from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.left_player_score = 0
    self.right_player_score = 0

  def update_score(self):
    self.clear()
    self.goto(-100,200)
    self.write(self.left_player_score,
               align="center",
               font=("Courier", 80, "normal"))
    self.goto(100,200)
    self.write(self.right_player_score,
               align="center",
               font=("Courier", 80, "normal"))