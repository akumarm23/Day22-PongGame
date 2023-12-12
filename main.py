# PONG GAME PYTHON v0.1

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.title("PONG GAME v0.1")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles, ball, and score object
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

# Listen for keyboard input
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    # If Right Paddle Misses
    if ball.xcor() > 380:
        ball.rest()
        score.l_point()
    
    # If Left Paddle Misses
    if ball.xcor() < -380:
        ball.rest()
        score.r_point()

# Exit the game on click
screen.exitonclick()
print("\033c", end="")
# END OF main.py CODE
