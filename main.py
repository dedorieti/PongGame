from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup
# Create all elements of the game
screen = Screen()
paddle_right = Paddle(side="right")
paddle_left = Paddle(side="left")
ball = Ball()
scoreboard_left = Scoreboard()
scoreboard_right = Scoreboard()
game_is_on = True

screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

# Move the paddles
screen.listen()
screen.onkey(paddle_right.paddle_up, "Up")
screen.onkey(paddle_right.paddle_down, "Down")

screen.onkey(paddle_left.paddle_up, "w")
screen.onkey(paddle_left.paddle_down, "s")

scoreboard_left.write_score(0, (-100, 200))
scoreboard_right.write_score(0, (100, 200))

# Start the game
screen.update()

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with the wal
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with the paddle
    if (paddle_left.distance(ball) < 20 and ball.xcor() < -320) or \
            (paddle_right.distance(ball) < 50 and ball.xcor() > 320):
        ball.smash()

    # Score points
    if ball.xcor() > 380:
        paddle_left.score += 1
        scoreboard_left.write_score(paddle_left.score, (-100, 200))
        time.sleep(1)
        ball.reset_position()
    if ball.xcor() < -380:
        paddle_right.score += 1
        scoreboard_right.write_score(paddle_right.score, (100, 200))
        time.sleep(1)
        ball.reset_position()


screen.exitonclick()
