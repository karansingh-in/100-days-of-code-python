import turtle as t

screen = t.Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
starting_position = [(0,0), (-20,0), (-40,0)]

segments = []
for position in starting_position:
    new_part = t.Turtle()
    new_part.shape('square')
    new_part.color('white')
    new_part.penup()
    new_part.goto(position)
    segments.append(new_part)

game_running = True
while game_running:
    for parts in segments:
        parts.forward(20)




screen.exitonclick()
