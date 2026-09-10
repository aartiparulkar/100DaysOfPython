import random
import time
from turtle import Screen, Turtle

from random_shapes import generate_random_color

choices = [1, -1]
turns = [0, 90, 180, 270]

steps = 500

time.sleep(5)
tim = Turtle()
screen = Screen()
screen.title("Turtle Random Walk")
screen.colormode(255)
tim.pensize(15)
tim.hideturtle()
tim.speed(0)


for i in range(steps):
    tim.pencolor(generate_random_color())
    position = random.choice(choices) * 30
    
    if (tim.position()[0] + position) > 350 and tim.heading() == 0:
        tim.seth(180)
        tim.forward(abs(position))
        print("Oops... right wall here")
        continue
    
    if (tim.position()[0] + position) < -350 and tim.heading() == 180:
        tim.seth(0)
        tim.forward(abs(position))
        print("Oops... left wall here")
        continue
    
    if (tim.position()[1] + position) > 350 and tim.heading() == 90:
        tim.seth(270)
        tim.forward(abs(position))
        print("Oops... upper wall here")
        continue
        
    if (tim.position()[1] + position) < -350 and tim.heading() == 270:
        tim.seth(90)
        tim.forward(abs(position))
        print("Oops... lower wall here")
        continue
        
    tim.forward(position)
    tim.seth(random.choice(turns))

print("Done!")
screen.exitonclick()
