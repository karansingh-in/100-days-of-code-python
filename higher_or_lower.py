import random
game_data = {
    "Cristiano Ronaldo": 630_000_000,
    "Lionel Messi": 520_000_000,
    "Selena Gomez": 420_000_000,
    "Taylor Swift": 310_000_000,
    "Kylie Jenner": 380_000_000,
    "The Rock": 390_000_000,
}
people = []
for char in game_data:
    people.append(char)
score = int(0)
correct_choice = ""
flag = True
while flag == True:
    choice_for_A = random.randint(0,len(people))
    print(f'compare A: {people[choice_for_A]}')
    print('VS')
    choice_for_B = random.randint(0,len(people))
    while choice_for_A == choice_for_B:
            choice_for_B = random.randint(0,len(people))
    print(f'compare B: {people[choice_for_B]}')
    
    if game_data[people[choice_for_A]] > game_data[people[choice_for_B]]:
        correct_choice = 'A'
    else:
        correct_choice = 'B'
    print('Who has more followers? A or B:')
    ans = input()
    if ans == correct_choice:
        print(f'You are right! Your score = {score}')
        score += 1
    else:
        print(f'Sorry that was wrong, Final score = {score}')
        flag = False
        


