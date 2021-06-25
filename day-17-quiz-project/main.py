from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_n = Question(data["question"], data["correct_answer"])
    question_bank.append(question_n)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz\nYour final score is {quiz.score}/{quiz.question_number}")
