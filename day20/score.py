from turtle import Turtle

FONT = ("MS Gothic", 24, "bold")
ALIGNMENT = "left"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.teleport(-320, 215)
        self.write_score()
    
    
    def update_score(self):
        self.score += 1    
        self.write_score()
        
        
    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.teleport(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
        