import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

your_cards = []
pc_cards = []
def game():
    pc_cards.append(ranks[random.randint(0,12)])
    your_cards.append(ranks[random.randint(0,12)])
    your_cards.append(ranks[random.randint(0,12)])
    flag = True
    while flag:  
        print(f'Your cards: {your_cards}')
        print(f'Computers cards: {pc_cards}')
        print('type "y" to get another card, "n" to pass: ')
        choice = input()
        if choice == 'y':
            flag = True
            pc_cards.append(ranks[random.randint(0,12)])
            your_cards.append(ranks[random.randint(0,12)])
        elif choice == 'n':
            your_sum = int(0)
            pc_sum = int(0)
            print(f'Your final hand: {your_cards}')
            print(f'PCs final hand: {pc_cards}')
            for card in your_cards:
                if (card == 'Jack' or card == 'Queen' or card == 'King' or card == 'Ace'):
                    your_sum = your_sum + 10
                else:
                    your_sum = your_sum + int(card)
            for card in pc_cards:
                if (card == 'Jack' or card == 'Queen' or card == 'King' or card == 'Ace'):
                    pc_sum = pc_sum + 10
                else:
                    pc_sum = pc_sum + int(card)
            if(abs(your_sum - 23)> abs(pc_sum)):
                print('Computer Wins!')
            elif(abs(your_sum - 23)< abs(pc_sum)):
                print('You Win!')        
            else:
                print('Its a Draw!')
            
            flag = False
            print('Do you want to play a game of BlackJack? Type y or n')
            more = input()
            if more == 'y':
                game()
                    
                
game()
            

            
            
    
        

    

