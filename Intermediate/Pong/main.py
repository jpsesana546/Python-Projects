from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

if __name__ == '__main__':
  
  # Create game screen  
  screen = Screen()
  screen.setup(width=800,height=600)
  screen.bgcolor("black")
  screen.title("Pong")
  screen.tracer(0)

  # Creating paddles
  right_paddle = Paddle(position=(350,0))
  left_paddle = Paddle(position=(-350,0))
  
  # Creating the ball
  ball = Ball()
  
  #Creating the scoreboard
  scoreboard = Scoreboard()
  scoreboard.update_score()

  # Moving the paddles
  screen.listen()
  screen.onkeypress(right_paddle.move_up, "Up")
  screen.onkeypress(right_paddle.move_down, "Down")
  screen.onkeypress(left_paddle.move_up, "w")
  screen.onkeypress(left_paddle.move_down, "s")

  # Refreshing the game screen
  game_is_on = True
  while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect top and bottom wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
      ball.y_direction *= -1

    # Detect collision with paddles
    elif (ball.distance(left_paddle) < 50 and ball.xcor() < -320 or 
          ball.distance(right_paddle) < 50 and ball.xcor() > 320):
      ball.x_direction *= -1
      ball.move_speed *= 0.9

    # Detect right side goal
    elif ball.xcor() > 380:
      ball.reset_position()
      scoreboard.left_player_score += 1
      scoreboard.update_score()

    # Detect left side goal
    elif ball.xcor() < -380:
      ball.reset_position()
      scoreboard.right_player_score += 1
      scoreboard.update_score()

      
  # Close application
  screen.exitonclick()