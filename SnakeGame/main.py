from turtle import Screen
from food import Food
from scoreboard import Scoreboard

import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

snake= Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	#detact collisions with food
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend_snake()
		score.increase_score()


	#Detact collisions with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		score.reset()
		snake.reset()

	#Detact collisions with Tail
	collision = snake.segments[1:]
	for segment in collision:
		if snake.head.distance(segment) < 10:
			score.reset()
			snake.reset()

screen.exitonclick()