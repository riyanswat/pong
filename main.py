from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard


# Screen
screen = Screen()
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
screen.setup(width=800, height=600)

# Objects:
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
# When you press and hold the corresponding key, it might not work, i think changing onkey to onkeypress might solve that issue (i havent tried it yet)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        ## Optional:
        # scoreboard.game_over()
        game_is_on = False

    # if r_paddle.ycor() > 250 or l_paddle.ycor() > 250:
    #     game_is_on = False

screen.exitonclick()
