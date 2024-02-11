from turtle import Turtle
import time


class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.goto(0,0)
    self.move_speed = 0.1
    self.y_direction = 10
    self.x_direction = 10

  def move(self):
    new_x = self.xcor() + self.x_direction
    new_y = self.ycor() + self.y_direction  

    self.goto(new_x, new_y)

  def reset_position(self):
    self.goto(0,0)
    self.x_direction *= -1
    self.move_speed = 0.1
