from data import question_data


class QuizBrain:
    def __init__(self, list_of_que):
        self.question_no = int(0)
        self.question_list = list_of_que
        self.score = int(0)
        
    def check_ans(self, answer1):
        if answer1.lower() == self.question_list[self.question_no - 1].answer.lower():
            self.score += 1
            print('Yay! You got it right')
        else: 
            print(f'Oops! The correct answer was {self.question_list[self.question_no - 1].answer}')

        print(f'Score: {self.score}/{self.question_no - 1}\n')
        
            
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f'Q.{self.question_no}: {current_question.question} (True/False): ')
        self.check_ans(user_ans)
        
        
    def still_has_questions(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            print("You've successfully completed the quiz")
            print(f'Your final score: {self.score}/{self.question_no - 1}')
            return False
        

