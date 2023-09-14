from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Creating a object
quiz = Quiz_brain(question_bank)
quiz.next_question()

score = 0
while quiz.is_question_left():
    quiz.next_question()

print(f"You have completed the quiz. Score : {quiz.score}")