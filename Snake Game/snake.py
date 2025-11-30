import turtle as t


class Snake():
    screen = t.Screen()
    starting_position = [(0,0), (-20,0), (-40,0)]
   # screen.tracer(0) # stops auto refresh of screen

    segments = []

    for position in starting_position:
        new_part = t.Turtle()
        new_part.shape('square')
        new_part.color('white')
        new_part.penup()
        new_part.goto(position)
        segments.append(new_part)
    screen.update() # force screen refresh

    def move(self):
        segments = Snake.segments
        screen = Snake.screen
        for i in range(len(segments) - 1, 0, -1): # in range(start, end, step)
            past_x = segments[i-1].xcor() # x coordiante of the last block
            past_y = segments[i-1].ycor() # y coordinate of the last block
            segments[i].goto(past_x, past_y) # new segment moving to the position of old block
        segments[0].forward(20) # moves block one forward, the rest follow along
        #segments[0].left(90)
        
        screen.listen()
        screen.onkey(segments[0].left(90), 'a')
        screen.onkey(segments[0].left(270), 'd')