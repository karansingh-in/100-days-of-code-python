print('Welcoe to the secrete auction program')
auction = {}
def ask():
    print('what is your name? ')
    name = input()
    print('whats ur bid? $')
    bid = int(input())
    auction[name] = bid
    print('Are there any more bidders? Type yes or no ')
    reponse = input()
    if reponse == 'yes':
        ask()
    elif reponse == 'no':
        max_bid = int(0)
        max_bidder = ''
        
        for name in auction:
            if auction[name] > max_bid:
                max_bid = auction[name]
                max_bidder = name
                
        print(f'The auction is won by {max_bidder} for bid ${max_bid}')
                            
ask()
    


    



