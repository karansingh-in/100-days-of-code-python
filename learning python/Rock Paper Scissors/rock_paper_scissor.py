# using random functions
import random

random_0_to_1 = random.random() #generates a random number between 0 and 1, inclusive of 0 only
random_0_to_10 = random.random() * 10 #now this will make it x10 so it'll be b/w 0 and 10, inclusive of 0 only

random_float = random.uniform(2,44) #generates a random float number b/w a, b inclusive of both
random_int = random.randint(0,1) #generates a random integer, inclusive of a, b

# rock paper scissor
print('What do you choose? 1 for rock, 2 for paper, 3 for scissor ')
choice = int(input())
choice -= 1
choice_m = random.randint(0,2)


inventory = ['rock', 'paper', 'scissor']
choice_of_user = inventory[choice]
choice_of_machine = inventory[choice_m]

print('choice of user: ', choice_of_user)
print('choice of machine: ', choice_of_machine)

if (choice == choice_m):
    print('tie')
elif ((choice == 0 and choice_m == 1) or (choice == 1 and choice_m == 2) or (choice == 2 and choice_m == 0)):
    print('machine wins')
else:
    print('user wins')
            





