import turtle as t
import time
from snake import Snake
from food import Food
screen = t.Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
saap = Snake()
khana = Food()

#khana.__init__()
khana.place_food()
game_running = True
while game_running:
    
    position_of_snake = saap.segments[0].pos()
    print(position_of_snake, khana.position_of_food)
    
    if(int(position_of_snake[0]) == int(khana.position_of_food[0]) and int(position_of_snake[1]) == int(khana.position_of_food[1])):
        #multiplier = int(len(saap.starting_position))
        print('kha liyeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        khana.place_food()
        #saap.starting_position.append()
    saap.move() # the fucntion should has 'self' in it s decleration else it throws an error that 0 arguments were expected but 1 was given because self argument is given by default to the function whenever the function is called
    screen.update() # when all the parts move a step forward the screen refreshes 
    time.sleep(0.1) # this makes the screen refresh delay time to 0.1 sec so the snake looks faster


    screen.listen()
    screen.onkey(saap.up, 'Up')
    screen.onkey(saap.down, 'Down')
    screen.onkey(saap.left, 'Left')
    screen.onkey(saap.right, 'Right')

   

screen.exitonclick()



