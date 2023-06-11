from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
#setup the screensize
screen.setup(width=500, height=400)
betturtle = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

#color list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
newyposition = -100
for color in colors:
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(color)
	new_turtle.penup()
	new_turtle.goto(x=-230, y= newyposition)
	newyposition += 30
	turtle_list.append(new_turtle)


if betturtle:
	is_race_on = Turtle

while is_race_on:

	for turtlec in turtle_list:
		if turtlec.xcor() >= 230:
			is_race_on = False
			winning_color = turtlec.pencolor()
			if(winning_color == betturtle):
				print(f"You have won the bet. The winning turtle color is {winning_color}")
			else:
				print(f"You have lost the bet. The winning turtle color is {winning_color}")

		random_step = random.randint(0,10)
		turtlec.forward(random_step)

screen.exitonclick()