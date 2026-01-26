import random

print('welcome to the number-guessing-game')
print('im thinking of a number between 1 and 100')
num = random.randint(0,101)

print('pssst, the number is ', num)


chances = int(0)
print('Choose a difficulty level. Type "easy" or "hard"')
type = input()
if type == 'hard':
    chances = 5
else:
    chances = 10
    
while chances > 0:
    print(f'You have {chances} attempt/s remaining to guess the number.')
    print('Make a guess')
    guess = int(input())
    chances -= 1
    if num - guess > 0:
        print('Too low\n Guess again.')
    elif num - guess < 0:
        print('Too high\n Guess again')
    else:
        print(f'You got it, The ans was {num}.')
        break
        
if chances == 0:
        print('You have run out of guesses. You lose.')
        
        
    

