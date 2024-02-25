from turtle import Turtle


class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.penup()
    self.shapesize(stretch_wid=5,stretch_len=1)
    self.goto(position)
    self.move_speed = 25

  def move_up(self):
    new_y = self.ycor() + self.move_speed
    self.goto(self.xcor(), new_y)

  def move_down(self):
    new_y = self.ycor() - self.move_speed
    self.goto(self.xcor(), new_y)
