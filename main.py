from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Project")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect the Collision btw food and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    #Detech collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score_board.game_over()
        game_is_on = False

    #Detect collision  of snake with itself
    for turtle in snake.turtles:
        if turtle == snake.head:
            pass
        elif snake.head.distance(turtle) <10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
