#TODO: 1. main file: create screen.
#TODO: 2. class for the paddle
    #TODO: 3. create and move paddle
        # create another one
#TODO: 4. class for the ball
    #create the ball and make it move
#TODO: 5. main file: collision with walls & bounce
    # collision with paddles & bounce
#TODO: 6. class for the scoreboard
#TODO: 7. main file: when the score goes up.
    # detect when paddle misses

from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

STARTING_POSITION_1 = (370, 0)
STARTING_POSITION_2 = (-380, 0)
MAX_SCORE = 7

ball = Ball()
r_paddle = Paddle(STARTING_POSITION_1)
l_paddle = Paddle(STARTING_POSITION_2)
scoreboard = Scoreboard()
screen = Screen()

screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() 
    # Collision with paddles
    if ball.distance(r_paddle) < 55 and ball.xcor() > 340 or ball.distance(l_paddle) < 55 and ball.xcor() < -350:
        ball.bounce_x()
    # Scoring a point
    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            scoreboard.l_score += 1
            scoreboard.update_scoreboard()
        elif ball.xcor() < -400:
            scoreboard.r_score += 1
            scoreboard.update_scoreboard()
        ball.reset()
        ball.bounce_x()
    # Finishing the game
    if MAX_SCORE in (scoreboard.r_score, scoreboard.l_score):
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
