import turtle as t
import time
class Snake():
    screen = t.Screen()
    def __init__(self):
        self.starting_position = [(0,0), (-20,0), (-40,0)]            
        self.segments = []
        for position in self.starting_position:
            self.extend_tail(position)
        self.screen.update() # force screen refresh
        time.sleep(0.1)
    def extend_tail(self, position):
        new_part = t.Turtle()
        new_part.shape('square')
        new_part.color('pink')
        new_part.penup()
        new_part.goto(position)
        self.segments.append(new_part)
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1): # in range(start, end, step)
            past_x = self.segments[i-1].xcor() # x coordiante of the last block
            past_y = self.segments[i-1].ycor() # y coordinate of the last block
            self.segments[i].goto(past_x, past_y) # new segment moving to the position of old block
        self.segments[0].forward(20) # moves block one forward, the rest follow along
    def up(self):
        self.segments[0].setheading(0)
        self.segments[0].left(90) # moves block one forward, the rest follow along   
    def down(self):
        self.segments[0].setheading(0)
        self.segments[0].left(270) # moves block one forward, the rest follow along
    def left(self):
        self.segments[0].setheading(0)
        self.segments[0].left(180) # moves block one forward, the rest follow along
    def right(self):
        self.segments[0].setheading(0)
            
            
            