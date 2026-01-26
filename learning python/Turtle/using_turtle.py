from turtle import Turtle, Screen
import random

tom = Turtle()
screen = Screen()
screen.bgcolor('black')
tom.shape('turtle')
tom.color('red')
tom.width(10)

def draw_square():
    for i in range(4):    
        tom.fd(150)
        tom.right(90)

def dashed():
    for i in range(12):
        tom.fd(10)
        tom.penup()
        tom.fd(10)
        tom.pendown()
        
def shapes():
    tom.width(10)
    color_for_turtle = ['red', 'blue', 'pink', 'green', 'black', 'purple']
    for i in range(3,11):
        sides = int(360/i)
        if 360 % i == 0:
            for j in range(i):
                tom.fd(100)
                tom.right(sides)
            tom.color(random.choice(color_for_turtle))
            
def random_walk():
    tom.width(10)
    color_for_turtle = ['red', 'blue', 'pink', 'green', 'black', 'purple', 'cyan', 'lime']
    dir = ['l', 'r']
    tom.speed('fastest')
    for i in range(100):
        tom.fd(40)
        turn = random.choice(dir)
        if turn == 'l':
            tom.left(90)
        else:
            tom.right(90)
        tom.color(random.choice(color_for_turtle))

def spirograph():
    tom.width(0)
    tom.speed('fastest')
    color_for_turtle = ['red', 'blue', 'pink', 'green', 'black', 'purple', 'cyan', 'lime', 'white']
    tom.shape('circle')
    for i in range(72):
        tom.right(5)
        for j in range(36):
            tom.fd(15)
            tom.right(10)
        tom.color(random.choice(color_for_turtle))
    
    

        
        
        
# draw_square()
# dashed()
# shapes()
# random_walk()
spirograph()



screen.exitonclick()


