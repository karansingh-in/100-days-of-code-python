import turtle as t
import time

screen = t.Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
starting_position = [(0,0), (-20,0), (-40,0)]
screen.tracer(0) # stops auto refresh of screen

segments = []

for position in starting_position:
    new_part = t.Turtle()
    new_part.shape('square')
    new_part.color('white')
    new_part.penup()
    new_part.goto(position)
    segments.append(new_part)
screen.update() # force screen refresh

game_running = True
while game_running:
    
    for i in range(len(segments) - 1, 0, -1): # in range(start, end, step)
        past_x = segments[i-1].xcor() # x coordiante of the last block
        past_y = segments[i-1].ycor() # y coordinate of the last block
        segments[i].goto(past_x, past_y) # new segment moving to the position of old block
    segments[0].forward(20) # moves block one forward, the rest follow along
    #segments[0].left(90)
    
    screen.listen()
    screen.onkey(segments[0].left(90), 'a')
    screen.onkey(segments[0].left(270), 'd')

    screen.update() # when all the parts move a step forward the screen refreshes 
    time.sleep(0.1) # this makes the screen refresh delay time to 0.1 sec so the snake looks faster 
    


screen.exitonclick()



