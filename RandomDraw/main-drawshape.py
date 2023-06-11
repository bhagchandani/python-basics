from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("classic")
timmy.color("red")
timmy.speed(1)
screen = Screen()
screen.colormode(255)
# for _ in range(1,10):
# 	timmy.forward(10)
# 	timmy.color("white")
# 	timmy.forward(10)
# 	timmy.color("red")

# for _ in range(1,10):
# 	timmy.forward(10)
# 	timmy.penup()
# 	timmy.forward(10)
# 	timmy.pendown()

def change_color():
    R = random.randint(0,255)
    B = random.randint(0,255)
    G = random.randint(0,255)

    timmy.color(R, G, B)


def draw_shape(sides):
	angle = 360/sides
	for turn in range(sides):
		timmy.forward(100)	
		timmy.right(angle)


for side in range(3,10):
	draw_shape(side)
	change_color()


screen.exitonclick()