from question_model import Question
from data import question_data # question_data is a list of dictionaries which contains keys 'text', 'answer'
from quiz_brain import QuizBrain

question_bank = [] # a list of objects
for que in question_data:
    question = que["text"]
    ans = que["answer"]
    obj = Question(question, ans) 
    question_bank.append(obj) # appending objects to a list
    
    
q1 = QuizBrain(question_bank)
while q1.still_has_questions():
    q1.next_question()

    
