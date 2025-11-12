def add(a,b):
    return int(a+b)
def sub(a,b):
    return int(a-b)
def multiply(a,b):
    return int(a*b)
def divide(a,b):
    return int(a/b)

operations = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': divide
}
def calcualtor():
    print('whats the first number? ')
    num1 = int(input())
    should_i_run = True

    while should_i_run:
        print('+')
        print('-')
        print('*')
        print('/')
        print('Pick an operation')
        operation = input()
        print('Enter the second number')
        num2 = int(input())
        ans = int(operations[operation](num1, num2))
        print(f'{num1} {operation} {num2} = {ans}')
        print(f'do u want ot continue with {ans} then press "y" or else press "n" to start a new calculation')
        choice  = input()
        if choice == 'y':
            num1 = ans
        else:
            calcualtor()

calcualtor()
    



