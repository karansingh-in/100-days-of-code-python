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
choice_for_A = random.randint(0,len(people)-1)

while flag == True:
    print(f'compare A: {people[choice_for_A]}')
    print('VS')
    choice_for_B = random.randint(0,len(people)-1)
    while choice_for_A == choice_for_B:
            choice_for_B = random.randint(0,len(people))-1
    print(f'compare B: {people[choice_for_B]}')
    
    if game_data[people[choice_for_A]] > game_data[people[choice_for_B]]:
        correct_choice = 'A'
        choice_for_A = choice_for_B
    else:
        correct_choice = 'B'
        choice_for_A = choice_for_A
    print('Who has more followers? A or B:')
    ans = input()
    if ans == correct_choice:
        score += 1
        print(f'You are right! Your score = {score}')
        # choice_for_A = choice_for_B
    else:
        print(f'Sorry that was wrong, Final score = {score}')
        flag = False
        


