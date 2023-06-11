from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Welcome to Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()

ball = Ball()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#to continue the game is on
game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(ball.move_speed)
	ball.move()

	#Detact collisions with TOP and BOTTOM
	if(ball.ycor() > 280 or ball.ycor() < -280):
		ball.bounce_y()

	#Detact collisions with paddle
	if(ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
		ball.bounce_x()

	#Detact r paddle misses
	if ball.xcor() > 380:
		ball.start_again()
		scoreboard.l_point()		

	#Detact l paddle misses
	if ball.xcor() < -380:
		ball.start_again()
		scoreboard.r_point()			

	
screen.exitonclick()