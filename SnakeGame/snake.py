from turtle import Turtle
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

	#Direction Based on Counter Clockwise
	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		for position in STARTING_POSITION:
			self.add_segment(position)

	def add_segment(self, position):
		segment = Turtle(shape="square")
		segment.color("White")
		segment.penup()
		segment.goto(position)
		self.segments.append(segment)

	def extend_snake(self):			
		self.add_segment(self.segments[-1].position())		

	def move(self):
		for seg_num in range(len(self.segments) - 1,0,-1):
			lastSegmentX = self.segments[seg_num-1].xcor()
			lastSegmentY = self.segments[seg_num-1].ycor()
			self.segments[seg_num].goto(lastSegmentX, lastSegmentY)

		self.head.forward(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def reset(self):
		for seg in self.segments:
			seg.goto(1000, 1000)
		self.segments.clear()
		self.create_snake()
		self.head = self.segments[0]

