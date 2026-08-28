import math
from turtle import *


SKY_BLUE = "#55c4e6"
YELLOW = "#ffe165"
CARD_GREEN = "#98bb5d"
LIGHT_GREY = "#c9caca"
BLACK = "#070d03"
DARK_GREEN = "#315c32"


def draw_card_rectangle(length, curve_length):
    """Draw the outline of a Pokémon card."""
    for _ in range(2):
        fd(length)
        right(45)
        fd(curve_length)
        right(45)
        fd(length * 1.4)
        right(45)
        fd(curve_length)
        right(45)


def fill_card(fill_color, length, curve_length):
    """Draw and fill a Pokémon card section."""
    color(fill_color)
    begin_fill()
    draw_card_rectangle(length, curve_length)
    end_fill()


def draw_card():
    """Draw the outer and inner card."""
    teleport(-250, 365)
    pensize(3)
    fill_card(YELLOW, 500, 20)

    teleport(-242, 347)
    fill_card(CARD_GREEN, 485, 10)


def draw_bulb():
    """Draw Bulbasaur's dark-green bulb behind its body."""

    teleport(-45, 250)
    pencolor(DARK_GREEN)
    fillcolor(DARK_GREEN)
    seth(110)
    begin_fill()

    # Left side
    for _ in range(25):
        right(5)
        fd(1)

    seth(0)
    left(10)
    fd(50)

    # Right side
    for _ in range(25):
        left(3)
        fd(1)

    right(145)
    forward(30)

    # Bottom
    for _ in range(30):
        left(1)
        fd(1)

    # Back to starting point
    for _ in range(50):
        right(3)
        fd(3)

    end_fill()


def draw_eye(x, y, mirror=False):
    """Draw one of Bulbasaur's triangular eyes."""
    pencolor(BLACK)
    fillcolor("#c63035")
    pensize(2)

    teleport(x, y)
    seth(90)

    begin_fill()

    if not mirror:
        left(15)
        fd(18)
        left(30)
        fd(25)
        left(120)
        fd(38)
        left(120)
        fd(25)
    else:
        right(15)
        fd(18)
        right(30)
        fd(25)
        right(120)
        fd(38)
        right(120)
        fd(25)

    end_fill()


# ---------------------- Setup ----------------------

speed(0)

# ---------------------- Pokemon Card ----------------------

draw_card()

teleport(-225, 302)
pencolor(LIGHT_GREY)
fillcolor(SKY_BLUE)
begin_fill()

width(5)
fd(451)
right(90)
fd(300)
right(90)
fd(451)
right(90)
fd(300)

end_fill()

# ---------------------- Bulbasaur ----------------------

draw_bulb()

color("#58b8b5")
pencolor("#51aaa9")
width(1)
begin_fill()

# Head
seth(90)

center = (-50, 200)
a, b = 70, 50

teleport(center[0] + a, center[1])

for i in range(360, 225, -1):
    x = center[0] + a * math.cos(math.radians(i))
    y = center[1] + b * math.sin(math.radians(i))
    goto(x, y)

pencolor(BLACK)

left(30)
fd(40)

seth(90)

for i in range(175, 165, -1):
    x = center[0] + a * math.cos(math.radians(i))
    y = center[1] + b * math.sin(math.radians(i))
    goto(x, y)

right(20)
fd(30)

# Ears
left(10)
fd(20)
right(100)
fd(30)
left(20)
fd(65)
left(25)
fd(30)

# Body
right(110)
fd(60)
left(25)
fd(70)
right(10)
fd(30)
right(10)
fd(30)

# ---------------------- Legs ----------------------

# Hind right paw
seth(180)
fd(40)

teleport(20, 150)
seth(280)

for _ in range(6):
    left(1)
    fd(6)

for _ in range(8):
    right(2)
    fd(6)

# Front right paw
seth(180)
fd(30)
right(65)
fd(50)

up()
back(20)

seth(180)
down()
fd(10)
left(80)
fd(20)

# Hind left paw
seth(180)
fd(40)
right(70)
fd(30)

left(135)
fd(40)

# Front left paw
seth(180)
fd(30)
right(85)
fd(60)

right(30)
fd(55)

end_fill()

# ---------------------- Face ----------------------

# Smile
teleport(-90, 190)
seth(0)
fd(80)

# Nose
teleport(-40, 205)
fd(2)

teleport(-53, 205)
back(2)

# Eyes
draw_eye(-68, 210)
draw_eye(-20, 210, mirror=True)

# ---------------------- Card Information ----------------------

# Name
up()
goto(-150, 310)
down()
write("Bulbasaur", font=("Comic Sans", 22, "bold"))

# HP
up()
goto(150, 310)
down()
write("HP", font=("Comic Sans", 8, "bold"))

up()
goto(165, 310)
down()
write("70", font=("Comic Sans", 22, "bold"))

# ---------------------- Attacks ----------------------

# Vine Whip icon
up()
goto(-200, -80)
down()

pencolor(BLACK)
fillcolor(DARK_GREEN)
begin_fill()
circle(10)
end_fill()

# Vine Whip
color(BLACK)

up()
goto(-75, -100)
down()
write("Vine Whip", font=("Comic Sans", 18, "bold"))

# Vine Whip damage
up()
goto(175, -100)
down()
write("10", font=("Comic Sans", 18, "bold"))

# Razor Leaf icon
up()
goto(-200, -155)
down()

pencolor(BLACK)
fillcolor(DARK_GREEN)
begin_fill()
circle(10)
end_fill()

# Razor Leaf
up()
goto(-75, -175)
down()
write("Razor Leaf", font=("Comic Sans", 18, "bold"))

# Razor Leaf damage
up()
goto(175, -175)
down()
write("20", font=("Comic Sans", 18, "bold"))


# ---------------------- Finish ----------------------

ht()
mainloop()
