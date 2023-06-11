from turtle import Turtle
ALIGNMENT = "center"
SCOREFONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0	
		self.high_score = self.read_high_score()	
		self.color("White")
		self.penup()
		self.goto(0, 270)
		self.hideturtle()
		self.write_score()

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			self.write_high_score()

		self.score = 0
		self.update_score()

	# def game_over(self):
	# 	self.goto(0, 0)
	# 	self.write("GAME OVER.", False, align=ALIGNMENT, font=SCOREFONT)
		

	def update_score(self):
		self.clear()		
		self.write_score()

	def write_score(self):	
		self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=SCOREFONT)

	def increase_score(self):
		self.score += 1
		self.update_score()

	def read_high_score(self):
		file = open("data.txt", mode="r")
		score = file.read()
		file.close()
		return int(score)


	def write_high_score(self):
		file = open("data.txt", mode="w")
		file.write(str(self.high_score))
		file.close()