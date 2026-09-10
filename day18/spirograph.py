from turtle import Screen, Turtle

from random_shapes import generate_random_color

tim = Turtle()
screen = Screen()
screen.title("Turtle Spirograph")
screen.colormode(255)
tim.speed(0)
for angle in range(0, 360, 5):
    tim.pencolor(generate_random_color())
    tim.seth(angle)
    tim.circle(radius=80)


screen.exitonclick()