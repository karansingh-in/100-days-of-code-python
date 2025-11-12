import turtle as t
from turtle import Screen
import random

screen = Screen()
tom = t.Turtle()
screen.bgcolor('black')
tom.shape('turtle')
tom.color('red')

tim = t.Turtle()
tim.shape('turtle')
tim.color('yellow')

tommy = t.Turtle()
tommy.shape('turtle')
tommy.color('blue')

timmy = t.Turtle()
timmy.shape('turtle')
timmy.color('pink')

screen.setup(width=500, height=400)
choice = screen.textinput(title='make a bet', prompt='which turtle will win? ')
tom.penup()
tommy.penup()
tim.penup()
timmy.penup()
tom.goto(-238, 0)
tommy.goto(-238, 40)
tim.goto(-238, 80)
timmy.goto(-238, -40)
tom.pendown()
tommy.pendown()
tim.pendown()
timmy.pendown()

def move():
    pace_tom = int(0)
    pace_tommy = int(0)
    pace_tim = int(0)
    pace_timmy = int(0)

    while (pace_tom < 500 and pace_tommy < 500 and pace_tim < 500 and pace_timmy < 500):
        move_tom = random.randint(1,4)
        move_tommy = random.randint(1,4)
        move_tim = random.randint(1,4)
        move_timmy = random.randint(1,4)
        
        tom.fd(move_tom)
        pace_tom += move_tom
        tommy.fd(move_tommy)
        pace_tommy += move_tommy
        tim.fd(move_tim)
        pace_tim += move_tim
        timmy.fd(move_timmy)
        pace_timmy += move_timmy
        
        if pace_tim>500:
            if choice == 'yellow':
                print('You win for choosing Yellow')
            else:
                print('You lost')
            
        elif pace_timmy>500:
            if choice == 'pink':
                print('You win for choosing Pink')
            else:
                print('You lost')
        elif pace_tom>500:
            if choice == 'red':
                print('You win for choosing Red')
            else:
                print('You lost')
        elif pace_tommy>500:
            if choice == 'blue':
                print('You win for choosing Blue')
            else:
                print('You lost')
move()
screen.exitonclick()
 