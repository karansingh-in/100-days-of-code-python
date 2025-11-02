import random


words = [
    "ocean", "matrix", "quantum", "fusion", "nebula", "python", "echo",
    "shadow", "binary", "crystal", "velocity", "zenith", "paradox",
    "glitch", "momentum", "gravity", "spectrum", "cyber", "vortex",
    "horizon", "stellar", "cascade", "cipher", "flare", "element",
    "serenity", "signal", "infinity", "spark", "pulse", "luminous",
    "fragment", "catalyst", "nexus", "arcane", "vertex", "aether",
    "drift", "phantom", "chrono", "nova", "pixel", "plasma", "ripple",
    "synthesis", "fractal", "silhouette", "orbit", "flux", "radiant"
]

chosen_word = random.choice(words)
list_of_chosen_word = list(chosen_word)
list_of_guesses = []
list_of_index = []
no_of_guesses = len(chosen_word)
no_of_right_guesses = int(0)

for words in chosen_word:
    list_of_guesses.append('_')
    
print('Welcome to the Hangman game')
print('A word has been chosen for you to guess: ', end='')
for blanks in range(len(chosen_word)):
    if blanks != len(chosen_word)-1:
    #    print('_', end='') # end= '' makes sure the next _ is printed on the same line
        # for char in list_of_guesses:
        #     print(char, end= '')
        print(list_of_guesses[blanks], end= '')
    else:
        print('_\n')
        # for char in list_of_guesses:
        #     print('_\n')
print(chosen_word)


while no_of_guesses != 0:
    user_choice = input()
    no_of_guesses -= 1
    
    for letters in list_of_chosen_word:
        if user_choice == letters:
            # print(user_choice, end= '')
            index = list_of_chosen_word.index(user_choice)
            if not index in list_of_index:
                list_of_guesses[index] = list_of_chosen_word[index]
                list_of_index.append(index)
                no_of_right_guesses += 1
                print('Very well! ')

    if not user_choice in list_of_chosen_word:
        print(f'Wrong choice, you have {no_of_guesses} / {len(chosen_word)} lives left.')
            
    for blanks in range(len(chosen_word)):
        if blanks != len(chosen_word)-1:
            print(list_of_guesses[blanks], end= '')
        else:
            print(list_of_guesses[len(chosen_word)-1])
            print('\n')

print()
if no_of_right_guesses == len(chosen_word):
    print('You have guessed the word right, You WON!')
else:
    print('You LOSE!')



