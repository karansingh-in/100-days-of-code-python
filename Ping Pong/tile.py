import turtle as t
import time
class Tile():
    screen = t.Screen()
    def __init__(self):
        self.segments = []
        self.create_box()
        self.create_box()
        self.create_box()
        self.create_box()
        self.create_box()
        self.screen.update()
        time.sleep(0.1)
        
    def create_box(self):
        self.box = t.Turtle()
        self.box.penup()
        self.box.shape('square')
        self.segments.append(self.box)
        self.box.color('white')

        
    def shift_to(self,position):
        self.segments[0].goto(position)
        self.segments[1].goto(position[0], position[1] - 20)
        self.segments[2].goto(position[0], position[1] - 40)
        self.segments[3].goto(position[0], position[1] - 60)
        self.segments[4].goto(position[0], position[1] - 80)
        
        
    def move_up(self):
        for i in range(len(self.segments) - 1, 0, -1): # in range(start, end, step)
            past_x = self.segments[i-1].xcor() # x coordiante of the last block
            past_y = self.segments[i-1].ycor() # y coordinate of the last block
            self.segments[i].goto(past_x, past_y) # new segment moving to the position of old block
        self.segments[0].setheading(0)
        self.segments[0].left(90)
        self.segments[0].forward(20) # moves block one forward, the rest follow along
        self.screen.update()
        time.sleep(0.1)
    

    def move_down(self):
        for i in range(0, len(self.segments) - 1, 1): # in range(start, end, step)
            past_x = self.segments[i+1].xcor() # x coordiante of the last block
            past_y = self.segments[i+1].ycor() # y coordinate of the last block
            self.segments[i].goto(past_x, past_y) # new segment moving to the position of old block
        self.segments[len(self.segments) - 1].setheading(0)
        self.segments[len(self.segments) - 1].left(270)
        self.segments[len(self.segments) - 1].forward(20) # moves block one forward, the rest follow along
        self.screen.update()
        time.sleep(0.1)
        
        
        
        
        
        
        


