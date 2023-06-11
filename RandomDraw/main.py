from turtle import Turtle, Screen
import random

def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)

	random_color = (r, g, b)
	return random_color

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.speed("fastest")

timmy.home()



while timmy.heading() != 350:
	timmy.color(random_color())
	timmy.circle(100)
	timmy.setheading(timmy.heading() + 10)




screen.exitonclick()