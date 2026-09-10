from random import randint
from turtle import Screen, Turtle


def generate_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)    


def draw_shape(sides, tim:Turtle):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)
    

if __name__ == "__main__":
    timmy = Turtle()
    screen = Screen()

    screen.colormode(255)
    timmy.pensize(2)
    timmy.teleport(-50, 150)

    for i in range(3, 10):
        timmy.pencolor(generate_random_color())
        draw_shape(sides=i, tim=timmy)

    screen.exitonclick()