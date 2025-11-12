print('welcome ot treasure island, you misson is to find the treasure')
choice1 = input('Type "left" or "right" ')
if choice1 == 'right':
    print('game over')
elif choice1 == 'left':
    print('you have come to a lake, there is an island in the middle of the lake.')
    choice2 = input('Type "swim" or "wait" ')
    if choice2 == 'swim':
        print('game over')
    elif choice2 == 'wait':
        print('you arrived at the island unharmed, there is a house with 3 doors.')
        choice3 = input('one red, one yellow, one blue. which color do you choose?')
        if choice3 == 'red':
            print('game over')
        elif choice3 == 'yellow':
            print('you win')
        elif choice3 == 'blue':
            print('game over')            

