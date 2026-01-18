import turtle as t
import time
from snake import Snake
from food import Food
import sys, os

# required to load the .gif file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

highscore = int(0)
main_loop = True
def game():
    try:
        if main_loop:
            screen = t.Screen()
            score = t.Turtle()
            ending = t.Turtle()
            restart = t.Turtle()
            bg_path = resource_path('background.gif')
            screen.addshape(bg_path)
            t.shape(bg_path)
            ending.color('white')
            ending.ht()
            score.color('white')
            score.penup()
            score.ht()
            restart.color('white')
            restart.penup()
            restart.ht()
            screen.setup(width=610, height=610)
            screen.bgcolor('black')
            screen.title('Snake Game')
            screen.tracer(0)
            saap = Snake()
            khana = Food()
            scorecard = int(0)
            score.goto(0,280)
            global highscore
            score.write(f"Highscore: {highscore} | Score: {scorecard}",  align='center', font=('Segoe UI', 15, 'normal'))
            khana.place_food()
            
            def quit():
                global main_loop
                main_loop = False
                
            game_running = True
            while game_running:
                position_of_snake = saap.segments[0].pos()
                if(abs(int(position_of_snake[0]) - int(khana.position_of_food[0])) < 15  and abs(int(position_of_snake[1]) - int(khana.position_of_food[1])) < 15):
                    position_of_tail = saap.segments[len(saap.segments) - 1].pos()
                    khana.place_food()
                    score.clear()
                    score.goto(0,280)
                    scorecard += 1
                    score.write(f"Highscore: {highscore} | Score: {scorecard}", align='center', font=('Segoe UI', 15, 'normal'))
                    saap.extend_tail(position_of_tail)
                if position_of_snake[0] > 285 or position_of_snake[0] < -285 or position_of_snake[1] > 285 or position_of_snake[1] < -285:
                    ending.write(f'Game Over!!\nwhy: you hit a wall', align='center', font=('Segoe UI', 24, 'normal'))
                    game_running = False
                for part in saap.segments:
                    if part != saap.segments[0] and part != saap.segments[1] and saap.segments[0].distance(part) < 10:
                        ending.write(f'Game Over!!\nwhy: you bit your tail', align='center', font=('Segoe UI', 24, 'normal'))
                        game_running = False
                saap.move() # the fucntion should has 'self' in it s decleration else it throws an error that 0 arguments were expected but 1 was given because self argument is given by default to the function whenever the function is called
                screen.update() # when all the parts move a step forward the screen refreshes 
                time.sleep(0.1) # this makes the screen refresh delay time to 0.1 sec so the snake looks faster
                screen.listen()
                screen.onkey(saap.up, 'Up') 
                screen.onkey(saap.down, 'Down')
                screen.onkey(saap.left, 'Left')
                screen.onkey(saap.right, 'Right')
                screen.onkey(saap.up, 'w') 
                screen.onkey(saap.down, 's')
                screen.onkey(saap.left, 'a')
                screen.onkey(saap.right, 'd')
            if not game_running:
                if scorecard > highscore:
                    highscore = scorecard
                time.sleep(2)
                screen.clear()
                screen.bgcolor('black')
                restart.write(f'The game will restart in 3 sec...\nPress "E" to exit', align='center', font=('Segoe UI', 15, 'bold'))
                time.sleep(2)
                screen.clear()
                screen.bgcolor('black')
                screen.listen()
                screen.onkey(quit, 'e')
                for i in range(3):
                    if main_loop:
                        restart.write(f'{abs(i-3)}', align='center', font=('Segoe UI', 20, 'bold'))
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('black')  
                        screen.listen()
                        screen.onkey(quit, 'e')
                    else:
                        break
                game()
    except:
        pass


if __name__ == '__main__':
    game()
    
