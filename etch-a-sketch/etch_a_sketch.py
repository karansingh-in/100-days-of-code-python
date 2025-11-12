from turtle import Turtle, Screen

screen = Screen()
tom = Turtle()

def move_forward():
    tom.fd(10)
def move_backward():
    tom.bk(10)
def turn_right():
    tom.right(10)
def turn_left():
    tom.left(10)
def clean():
    tom.home()
    tom.clear()
    
    
screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clean, 'c')


screen.exitonclick()

