import turtle as t
import time

class Ball():
    screen = t.Screen()
    def __init__(self):
        self.block = t.Turtle()
        self.block.color('white')
        self.block.shape('circle')
        self.block.penup()
        self.screen.update()
        
    def move_x(self, steps):
        time.sleep(0.1)
        self.block.setheading(0)
        self.block.forward(steps)
        
    def move_y(self, steps):
        time.sleep(0.1)
        self.block.setheading(0)
        self.block.left(90)
        self.block.forward(steps)
        


