from random import choice
from turtle import Screen, Turtle

from colorgram import extract

colors = extract("hirst_painting_palette.jpg", 15)

color = colors[5].rgb

tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.title("Turtle Hirst Painting")
tim.teleport(-280, -315)
tim.speed(0)
for i in range(10):
    tim.teleport(-300, tim.position()[1]+50)
    for j in range(10):
        tim.pencolor(choice(colors).rgb)
        tim.dot(20)
        tim.up()
        tim.forward(50)
        tim.down()
screen.exitonclick()