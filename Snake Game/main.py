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

def turn_left():
    i = int(0)
    while i<len(segments):
        segments[i].forward(20*(i+1))
        screen.update()
        time.sleep(0.1)
        j = i
        while not (j - 1 < 0):
            segments[j-1].forward(20)
            screen.update()
            time.sleep(0.1)
            j -= 1
        segments[i].left(90)
        i += 1


for parts in segments:
    parts.forward(50)
    screen.update()
    time.sleep(0.1)
    
turn_left()
# screen.update()
# time.sleep(0.1)

game_running = True
while game_running:
    for parts in segments:
        parts.forward(20)

    screen.update() # when all the parts move a step forward the screen refreshes 
    time.sleep(0.1) # this makes the screen refresh delay time to 0.1 sec so the snake looks faster 
    


screen.exitonclick()



