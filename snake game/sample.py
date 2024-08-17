from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def circle():
    tim.right(90)
    tim.forward(10)
    tim.right(90)
    tim.forward(10)


def c_clockwise():
    tim.left(90)
    tim.forward(100)
    tim.right(75)
    tim.forward(50)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=circle)
screen.onkey(key="a", fun=c_clockwise)
screen.exitonclick()
