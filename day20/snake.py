from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.length = 0
        self.create_snake()
        self.head = self.snake[0]
        
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    
    
    def move(self):
        for seg in range(self.length - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].teleport(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # 4. Control the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
        
    
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
        
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
            
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
            
    
    # 7. Grow the snake tail
    def add_segment(self, position):
        s = Turtle(shape="circle")
        s.color("white")
        s.penup()
        s.goto(position)
        self.snake.append(s)
        self.length += 1
        
        
    def extend(self):
        self.add_segment(self.snake[-1].position())
            