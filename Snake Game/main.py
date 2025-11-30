import turtle as t
import time
from snake import Snake
screen = t.Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
saap = Snake()


game_running = True
while game_running:
    

    saap.move() # the fucntion should has 'self' in it s decleration else it throws an error that 0 arguments were expected but 1 was given because self argument is given by default to the function whenever the function is called
    screen.update() # when all the parts move a step forward the screen refreshes 
    time.sleep(0.1) # this makes the screen refresh delay time to 0.1 sec so the snake looks faster 
    


screen.exitonclick()



