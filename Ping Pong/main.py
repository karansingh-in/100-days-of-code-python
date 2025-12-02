import turtle as t
from tile import Tile
import time

screen = t.Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Ping-Pong Game')
right_tile = Tile()
left_tile = Tile()
position_right = (780,0)
position_left = (-780,0)
right_tile.shift_to(position_right)
left_tile.shift_to(position_left)
screen.tracer(0)
screen.update()
time.sleep(0.1)
screen.listen()
screen.onkeypress(left_tile.move_up, "w")
screen.onkeypress(left_tile.move_down, 's')
screen.onkeypress(right_tile.move_up, "Up")
screen.onkeypress(right_tile.move_down, 'Down')


screen.exitonclick()
