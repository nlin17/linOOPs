from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()