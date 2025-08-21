from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

queston_bank = []
for i in range(len(question_data)):
    question = Question(question_data[i]["question"],question_data[i]["correct_answer"])
    queston_bank.append(question)

quiz = QuizzBrain(queston_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the Quiz")
print(f"Your Final score was: {quiz.score}/{quiz.question_number}")


