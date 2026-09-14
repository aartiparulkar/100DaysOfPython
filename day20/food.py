from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.65, stretch_wid=0.65)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
        
    
    def refresh(self):
        x = randint(-285, 285)
        y = randint(-200, 200)
        self.teleport(x, y)
            