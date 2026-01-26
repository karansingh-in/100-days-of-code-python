# question_data = [
#     {
#      "text": "A slug's blood is green.", 
#      "answer": "True"
#      },
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]


import requests
parameters = {
    'amount':100,
    'type':'boolean',
}

connection = requests.get('https://opentdb.com/api.php', params=parameters)
data = connection.json()

question_data = []
for i in range(len(data['results'])):
    question = data['results'][i]['question']
    ans = data['results'][i]['correct_answer']
    dict = {
        'text': question,
        'answer': ans
    }
    question_data.append(dict)
    
# print(question_data)
    
# print(question)
# print(ans)

# print(data)

# {'response_code': 0, 
#  'results': [
#      {
#          'type': 'boolean', 
#          'difficulty': 'easy', 
#          'category': 'Geography', 
#          'question': 'There are no deserts in Europe.', 
#          'correct_answer': 'True', 
#          'incorrect_answers': ['False']
#          }
#      ]
#  }


