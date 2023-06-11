from turtle import Turtle
import random

class Food(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len=0.5, stretch_wid=0.5)
		self.color("red")
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		"""As our window is 300X300 if we set the random limit
		by 300 but when snake try to catch the food it will hit the wall
		so we are setting the limit by 280"""

		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 280)
		self.goto(random_x, random_y)