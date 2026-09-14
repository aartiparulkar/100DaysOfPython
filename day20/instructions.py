from turtle import Turtle


class Instructions(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

        self.show_instructions()


    def show_instructions(self):
        self.goto(0, 80)
        self.write(
            "SNAKE CLASSIC",
            align="center",
            font=("MS Gothic", 28, "bold")
        )

        self.goto(0, 20)
        self.write(
            "W",
            align="center",
            font=("MS Gothic", 20, "bold")
        )

        self.goto(-35, -20)
        self.write(
            "A",
            align="center",
            font=("MS Gothic", 20, "bold")
        )

        self.goto(0, -20)
        self.write(
            "S",
            align="center",
            font=("MS Gothic", 20, "bold")
        )

        self.goto(35, -20)
        self.write(
            "D",
            align="center",
            font=("MS Gothic", 20, "bold")
        )

        self.goto(0, -80)
        self.write(
            "Click anywhere to start",
            align="center",
            font=("MS Gothic", 14, "normal")
        )