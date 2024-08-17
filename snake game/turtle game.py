import random
from turtle import Turtle, Screen

race = False
screen = Screen()
screen.setup(500, 400)
setting = screen.textinput("Make a bet", "Which turtle will win the race?")
clr = ["red", "orange", "blue", "green", "purple", "yellow"]
y = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(len(clr)):
    tim = Turtle(shape="turtle")
    tim.fillcolor(clr[i])
    tim.penup()
    tim.goto(x=-235, y=y[i])
    all_turtles.append(tim)

if setting:
    race = True

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 235:
            race = False
            win = turtle.fillcolor()
            if setting == win:
                print(f"You've won the game.{win} turtle won the race.")
            else:
                print(f"You've lost the game.{win} turtle won the race.")
        dist = random.randint(0,10)
        turtle.forward(dist)


screen.exitonclick()
