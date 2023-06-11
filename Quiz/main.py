from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questionrow in question_data:
	question_bank.append(Question(questionrow["question"], questionrow["correct_answer"]))


quiz = QuizBrain(question_bank)


while not quiz.still_has_question():
	quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
