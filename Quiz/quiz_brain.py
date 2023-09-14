class Quiz_brain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True / False): ")
        actual_answer = current_question.answer
        self.check(user_answer, actual_answer)

    def is_question_left(self):
        size = len(self.question_list)
        if self.question_number == size:
            return False
        return True

    def check(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            self.score += 1
            print("You are Right")
        else:
            print("You are wrong")
        print(f"The Correct answer : {actual_answer}")
        print(f"Your current Score : ({self.score}/{self.question_number})")
