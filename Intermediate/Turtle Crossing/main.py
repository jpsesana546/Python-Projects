import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

if __name__ == '__main__':
    # Screen setup
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Create player
    player = Player()

    #Create score board
    scoreboard = Scoreboard()
    scoreboard.write_score()

    # Player controls
    screen.listen()
    screen.onkeypress(player.move_up,"w")

    # Refresh screen
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        # Check if player crossed the road and uppdate score
        if player.ycor() > player.FINISH_LINE_Y:
            player.goto(player.STARTING_POSITION)
            scoreboard.score += 1
            scoreboard.write_score()

    screen.exitonclick()
