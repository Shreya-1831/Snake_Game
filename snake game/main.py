from turtle import Screen
from snake import Snake
import snake_food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = snake_food.snfood()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Check for collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    # Check for collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Check for collision with tail
    for segment in snake.seg:
        if segment == snake.head :
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
