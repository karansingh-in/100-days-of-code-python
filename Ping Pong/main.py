import turtle as t
from tile import Tile
from ball import Ball
import time

screen = t.Screen()
screen.bgcolor('black')
screen.setup(1700,800)
screen.title('Ping-Pong Game')
right_tile = Tile()
left_tile = Tile()
screen.tracer(0)
position_right = (780,0)
position_left = (-780,0)
right_tile.shift_to(position_right)
left_tile.shift_to(position_left)
screen.update()
time.sleep(0.1)

block = Ball()

game_running = True
while game_running:
    block.move_x()
    block.move_y()
    screen.update()

screen.listen()
screen.onkeypress(left_tile.move_up, "w")
screen.onkeypress(left_tile.move_down, 's')
screen.onkeypress(right_tile.move_up, "Up")
screen.onkeypress(right_tile.move_down, 'Down')


screen.exitonclick()


