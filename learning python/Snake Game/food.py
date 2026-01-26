import random
import turtle as t
class Food():
    def __init__(self):
        self.screen = t.Screen()
        self.apple = t.Turtle()
        self.apple.color('red')
        self.apple.shape('circle')
        self.apple.shapesize(0.6)
    def place_food(self):
        possible_positions = list(range(-250, 251, 20))
        x_position = round(random.choice(possible_positions)) * 1.00
        y_position = round(random.choice(possible_positions)) * 1.00
        self.position_of_food = (x_position,y_position)
        self.apple.penup()
        self.apple.goto(self.position_of_food)