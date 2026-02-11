from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "s")
screen.onkey(l_paddle.go_down, "w")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # if ball.ycor() > 300 or ball.ycor() < -300:

screen.exitonclick()