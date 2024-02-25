from turtle import Turtle

MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.FINISH_LINE_Y = 280
        self.STARTING_POSITION = (0, -280)
        self.goto(self.STARTING_POSITION)

    def move_up(self):
        # Player movement
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)