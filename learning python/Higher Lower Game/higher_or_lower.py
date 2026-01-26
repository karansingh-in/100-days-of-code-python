import random
game_data = {
    "Cristiano Ronaldo": 630_000_000,
    "Lionel Messi": 520_000_000,
    "Selena Gomez": 420_000_000,
    "Taylor Swift": 310_000_000,
    "Kylie Jenner": 380_000_000,
    "The Rock": 390_000_000
}
score = int(0)
correct_choice = ""
flag = True
choice_for_A = random.choice(list(game_data))

while flag == True:
    print(f'compare A: {choice_for_A}')
    print('VS')
    choice_for_B = random.choice(list(game_data))
    while choice_for_A == choice_for_B:
            choice_for_B = random.choice(list(game_data))
    print(f'compare B: {choice_for_B}')
    
    if game_data[choice_for_A] > game_data[choice_for_B]:
        correct_choice = 'A'
        choice_for_A = choice_for_B
    else:
        correct_choice = 'B'
        choice_for_A = choice_for_A
    print('Who has more followers? A or B:')
    ans = input().upper()
    if ans == correct_choice:
        score += 1
        print(f'You are right! Your score = {score}')
    else:
        print(f'Sorry that was wrong, Final score = {score}')
        flag = False
        


