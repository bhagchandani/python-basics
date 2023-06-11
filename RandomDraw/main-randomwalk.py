from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("classic")
timmy.speed(4)
timmy.pen(fillcolor="red", pencolor="red", pensize=5)
screen = Screen()
screen.colormode(255)

def change_color():
    R = random.randint(0,255)
    B = random.randint(0,255)
    G = random.randint(0,255)

    timmy.color(R, G, B)

angle_array = [0, 90, 180, 270]
for side in range(50):
	r_angle = random.choice(angle_array)
	timmy.setheading(r_angle)
	

	timmy.forward(40)
	change_color()

screen.exitonclick()