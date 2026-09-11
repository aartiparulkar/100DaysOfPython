from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
screen.title("Etch-A-Sketch")

def move_fd():
    tim.forward(10)
    
    
def move_bk():
    tim.backward(10)
    

def rotate_left():
    tim.left(10)
    

def rotate_right():
    tim.right(10)
    

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()
    
    
screen.onkey(key="Up", fun=move_fd)
screen.onkey(key="Down", fun=move_bk)
screen.onkey(key="Left", fun=rotate_left)
screen.onkey(key="Right", fun=rotate_right)
screen.onkey(key="c", fun=clear)

screen.listen()
screen.mainloop()
