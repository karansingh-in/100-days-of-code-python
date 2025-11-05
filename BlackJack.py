import random
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
your_cards = []
pc_cards = []
your_sum = int(0)
pc_sum = int(0)
def check_blackjack():
    global your_cards
    global pc_cards
    local_your_sum = int(0)
    local_your_cards = your_cards
    local_pc_cards = pc_cards
    local_pc_sum = int(0)
    for card in local_your_cards:
                if (card == 'Jack' or card == 'Queen' or card == 'King'):
                    local_your_sum = local_your_sum + 10
                elif card == 'Ace':
                    if local_your_sum + 11 > 21:
                        local_your_sum = local_your_sum + 1
                    else:
                        local_your_sum = local_your_sum + 11
                else:
                    local_your_sum = local_your_sum + int(card)
    for card in local_pc_cards:
                if (card == 'Jack' or card == 'Queen' or card == 'King'):
                    local_pc_sum = local_pc_sum + 10
                elif card == 'Ace':
                    if local_pc_sum + 11 > 21:
                        local_pc_sum = local_pc_sum + 1
                    else:
                        local_pc_sum = local_pc_sum + 11
                else:
                    local_pc_sum = local_pc_sum + int(card)
    if local_pc_sum == 21:
        return True
    elif local_your_sum == 21:
        return True
def result():
            global your_sum
            global your_cards
            global pc_cards
            global pc_sum
            print(f'Your final hand: {your_cards}')
            print(f'PCs final hand: {pc_cards}')
            for card in your_cards:
                if (card == 'Jack' or card == 'Queen' or card == 'King'):
                    your_sum = your_sum + 10
                elif card == 'Ace':
                    if your_sum + 11 > 21:
                        your_sum = your_sum + 1
                        print('Your Ace is taken as 1')
                    else:
                        your_sum = your_sum + 11
                        print('Your Ace is taken as 11')
                else:
                    your_sum = your_sum + int(card)
            for card in pc_cards:
                if (card == 'Jack' or card == 'Queen' or card == 'King'):
                    pc_sum = pc_sum + 10
                elif card == 'Ace':
                    if pc_sum + 11 > 21:
                        pc_sum = pc_sum + 1
                        print('Computers Ace is taken as 1')
                    else:
                        pc_sum = pc_sum + 11
                        print('Computers Ace is taken as 11')
                else:
                    pc_sum = pc_sum + int(card)
            if(((21 - your_sum > 21 - pc_sum) and not pc_sum > 21)  or your_sum > 21 or pc_sum == 21):
                print('Computer Wins!')
                print('pc:', pc_sum)
                print('you:',your_sum)
            elif(((21 - your_sum < 21 - pc_sum) and not your_sum > 21) or pc_sum > 21 or your_sum == 21):
                print('You Win!')
                print('pc:',pc_sum)
                print('you:',your_sum)       
            else:
                print('Its a Draw!')
                print('pc:',pc_sum)
                print('you:',your_sum)    
            print('Do you want to play a game of BlackJack? Type y or n')
            more = input()
            if more == 'y':
                your_cards.clear()
                pc_cards.clear()
                your_sum = int(0)
                pc_sum = int(0)
                game()
def game():
    global your_sum
    global your_cards
    global pc_cards
    global pc_sum
    pc_cards.append(ranks[random.randint(0,12)])
    pc_cards.append(ranks[random.randint(0,12)])
    your_cards.append(ranks[random.randint(0,12)])
    your_cards.append(ranks[random.randint(0,12)])
    if check_blackjack():
        result()
    flag = True
    while flag:  
        print(f'Your cards: {your_cards}')
        print('Computers cards: ',end= '')
        print('[',end= '')
        for number in range(len(pc_cards)-1):
            print("'", pc_cards[number], "', ",end= '')
        print(']')
        print('type "y" to get another card, "n" to pass: ')
        choice = input()
        if choice == 'y':
            pc_cards.append(ranks[random.randint(0,12)])
            your_cards.append(ranks[random.randint(0,12)])
            if check_blackjack():
                result()
        elif choice == 'n':
            local_pc_sum = int(0)
            for card in pc_cards:
                    if (card == 'Jack' or card == 'Queen' or card == 'King'):
                        local_pc_sum = local_pc_sum + 10
                    elif card == 'Ace':
                        if local_pc_sum + 11 > 21:
                            local_pc_sum = local_pc_sum + 1
                        else:
                            local_pc_sum = local_pc_sum + 11
                    else:
                        local_pc_sum = local_pc_sum + int(card)  
            while local_pc_sum < 16:
                for card in pc_cards:
                    if (card == 'Jack' or card == 'Queen' or card == 'King'):
                        local_pc_sum = local_pc_sum + 10
                    elif card == 'Ace':
                        if local_pc_sum + 11 > 21:
                            local_pc_sum = local_pc_sum + 1
                        else:
                            local_pc_sum = local_pc_sum + 11
                    else:
                        local_pc_sum = local_pc_sum + int(card)   
                pc_cards.append(ranks[random.randint(0,12)])
            result()
game()
            

            
            
    
        

    

