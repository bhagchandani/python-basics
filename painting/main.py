#import colorgram
from turtle import Turtle, Screen
import random
timmy = Turtle()


screen = Screen()
screen.colormode(255)

#once fetched the color command out the code and save the colors in list
# color_list = []
# colors = colorgram.extract('spot.jpg', 30)
# for color in colors:
# 	r = color.rgb.r
# 	g = color.rgb.g
# 	b = color.rgb.b
# 	color_list.append((r, g,b))
timmy.penup()
timmy.ht()

#color list is firtsly generated from the colorgram package. Which is installed via pip
color_list = [(239, 234, 226), (220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61), (197, 85, 112), 
(208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)]  

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.speed("fastest")
x_start = timmy.ycor()

for dots in range(1,101):
	timmy.dot(20, random.choice(color_list))
	timmy.forward(40)
	if(dots % 10 == 0):
		xcor = timmy.xcor()
		ycor = timmy.ycor()
		timmy.sety(ycor + 40)
		timmy.setx(x_start)

	


screen.exitonclick()