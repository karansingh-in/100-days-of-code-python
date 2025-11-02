print('Type "encode" to encode and "decode" to decode')
choice = input()


def encoding(num, message):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']
    
    changed_alphabets = []
    counter = int(0)

    for count in range(len(alphabets)):
        changed_alphabets.append(alphabets[count])
        
    for char in alphabets:
        if (counter + num) > 25:
            counter = counter - 26
        changed_alphabets[counter] = alphabets[counter + num]
        counter += 1
        
    encoded = ''
    for char in message:
        if char in alphabets:
            index = alphabets.index(char)
            encoded = encoded + changed_alphabets[index]
        else:
            encoded = encoded + char
        
    print('The encoded message is ', encoded)
    
    
def decoding(num, message):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']
    
    changed_alphabets = []
    counter = int(0)
    
    for count in range(len(alphabets)):
        changed_alphabets.append(alphabets[count])
        
    for char in alphabets:
        if (counter + num) > 25:
            counter = counter + num - 26
        changed_alphabets[counter] = alphabets[counter - num]
        counter += 1

        
    decoded = ''
    for char in message:
        if char in alphabets:
            index = alphabets.index(char)
            decoded = decoded + changed_alphabets[index]
        else:
            decoded = decoded + char
        
    print('The decoded message is ', decoded)
    
    
if choice == 'encode':
    print('Type your message')
    msg = input()
    print('Type the shift number')
    shift = int(input())
    
    encoding(shift, msg)
    
elif choice == 'decode':
    print('Type your message')
    msg = input()
    print('Type the shift number')
    shift = int(input())
    
    decoding(shift, msg)
    
    
    
