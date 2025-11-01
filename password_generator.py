# for loop with in range
# for num in range(0,10): # 0 inclusive, 10 exclusive
#      print(num)
    
# print('----')
# for even in range(0,10,2): # i = i + 2 for each step
#      print(even)    


# password generator
import random
print('Welcome to pyPasswordGenerator')
print('How many letters would you like in your password?')
letter_count = int(input())
print('How many numbers would u like in ur password?')
num_count = int(input())
print('how many pecial char would u like in ur password?')
char_count = int(input())

inventory = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
, '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~']
inventory2 =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~']
password = ''
case = []

total_count = int(letter_count+num_count+char_count)

char_limit = int(0)
letter_limit = int(0)
num_limit = int(0)
for count in range(0, total_count):
    
    # all available, only num char, only letter char, only num letter, only char, only letter, only num
    if ((char_limit <= char_count) and (num_limit <= num_count) and (letter_limit <= letter_count)):
        token = int(random.randint(0, len(inventory)))
        password = password + inventory[token]
        
        if (token < 26):
            letter_limit += 1
        elif (token >= 26 and token < 36):
            num_limit += 1
        else:
            char_limit += 1
    elif ((char_limit <= char_count) and (num_limit <= num_count) and (letter_limit > letter_count)):
        token = int(random.randint(26, len(inventory)))
        password = password + inventory[token]

        if (token >= 26 and token < 36):
            num_limit += 1
        else:
            char_limit += 1          
    elif ((char_limit > char_count) and (num_limit <= num_count) and (letter_limit <= letter_count)):
        token = int(random.randint(26, len(inventory)-29))
        password = password + inventory[token]

        if (token >= 26 and token < 36):
            num_limit += 1
        else:
            letter_limit += 1      
    elif((char_limit <= char_count) and (num_limit > num_count) and (letter_limit <= letter_count)):
        token = int(random.randint(0, len(inventory2)))
        password = password + inventory[token]
        
        if (token < 26):
            letter_limit += 1
        else:
            char_limit += 1       
    elif ((char_limit <= char_count) and (num_limit > num_count) and (letter_limit > letter_count)):
        token = int(random.randint(36, len(inventory)))
        password = password + inventory[token]
        char_limit += 1
    elif ((char_limit > char_count) and (num_limit <= num_count) and (letter_limit > letter_count)):
        token = int(random.randint(26, len(inventory)-29))
        password = password + inventory[token]
        num_limit += 1
    elif ((char_limit > char_count) and (num_limit > num_count) and (letter_limit <= letter_count)):
        token = int(random.randint(0, 26))
        password = password + inventory[token]
        letter_limit += 1
    else:
        break

print(password)    

