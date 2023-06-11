class QuizBrain:

	def __init__(self, question_list):
		self.question_number = 0
		self.question_list = question_list
		self.score = 0

	def still_has_question(self):
		return (len(self.question_list)) == self.question_number
			

	def next_question(self):
		currentanswer = self.question_list[self.question_number]
		self.question_number += 1
		user_answer = input(f"Q: {self.question_number}: {currentanswer.text}. (True/False): ")
		self.check_answer(user_answer, currentanswer.answer)

	def check_answer(self, useranswer, currentanswer):
		if(useranswer.lower() == currentanswer.lower()):
			print("You are Right!")
			self.score += 1
		else:
			print("You got it Wrong!")

		print(f"The correct answer was {currentanswer}")
		print(f"You current score is {self.score}/{self.question_number}")
		print("\n")
