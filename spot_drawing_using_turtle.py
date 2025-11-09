from turtle import Turtle, Screen


tom = Turtle()
tom.shape('turtle')
tom.color('red')
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
    for i in range(3,37):
        sides = int(360/i)
        if 360 % i == 0:
            for j in range(sides):
                tom.fd(10)
                tom.right(360/sides)
            
        
        
        
# draw_square()
# dashed()
shapes()





screen = Screen()
screen.exitonclick()


