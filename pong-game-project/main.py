from turtle import Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))



# paddle listeners
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# left paddle
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


# ball
ball = Ball()


# scoreboard
scoreboard = Scoreboard()

# Update paddle on screen
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect collision right wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
        #game_is_on = False
        #screen.update()
        pass

    # detect collision left wall
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()