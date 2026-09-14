import time
from turtle import Screen

from food import Food
from instructions import Instructions
from score import ScoreBoard
from snake import Snake

# 1. Screen Setup
screen = Screen()
screen.setup(width=680, height=510)
screen.bgcolor("black")
screen.title("Snake Classic")
screen.tracer(0)

# 2. Snake Body
snake = Snake()

# 5. Create Food
food = Food()

# 6. Create a Score Board
score = ScoreBoard()

# 8. Show instructions
instruction =  Instructions()

# 4. Control the snake    
screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")


def start_game(x, y):
    instruction.clear()
    screen.onclick(None)
    
    game_loop()
    

def game_loop():
    # 3. Move the snake - snake.py
    game_over = False
    while not game_over:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        # 5. Detect collision with food - grow snake condition
        if snake.head.distance(food) < 17:
            food.refresh()
            # 7. Grow the snake
            snake.extend()
            score.update_score()
            
        # 6. Detect wall collisions - game_over condition
        if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() > 235 or snake.head.ycor() < -235:
            game_over = True
            score.game_over()
            
        # 7. Detect collision with tail - game_over condition
        for segment in snake.snake[1:]:
            if snake.head.distance(segment) < 10:
                game_over = True
                score.game_over()

screen.onclick(start_game)
screen.mainloop()