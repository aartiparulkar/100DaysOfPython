from random import randint
from turtle import Screen, Turtle

is_race_on = False

screen = Screen()
screen.setup(width=580, height=400)
user_bet = screen.textinput(title="Bet on a Turtle", prompt="Which color turtle would you bet on?")

colors = ["violet", "purple", "blue", "green", "gold", "orange", "red"]
turtles = []

for c in colors:
    turt = Turtle(shape="turtle")
    turtles.append(turt)
    turt.color(c)
    turt.penup()
    turt.goto(-240, 120 - 40 * colors.index(c))

winner = turtles[0]

if user_bet:
    is_race_on = True

msg = ""
    
while is_race_on:
    for turt in turtles:
        if turt.xcor() >= 250:
            is_race_on = False
            winner = turt.pencolor()
            if user_bet.lower() == winner:
                msg = f"You won🤑! The {winner} is the winning turtle."
            else:
                msg = f"You lost😭. The {winner} is the winning turtle."

        step = randint(0, 10)
        turt.forward(step)
        
t = Turtle()
t.hideturtle()
t.penup()
t.write(arg=msg, move=False, align="center", font=('Arial', 16, 'normal'))
screen.mainloop()
