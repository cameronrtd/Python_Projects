import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # Detect collision with ground or ceiling
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330 or
            ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        speed *= 0.9
    # Detect when r_paddle misses
    if ball.xcor() > 381:
        ball.reset()
        scoreboard.l_point()
        scoreboard.clear()
        scoreboard.update()
        speed = 0.1
    # Detect when l_paddle misses
    if ball.xcor() < -381:
        ball.reset()
        scoreboard.r_point()
        scoreboard.clear()
        scoreboard.update()
        speed = 0.1









screen.exitonclick()