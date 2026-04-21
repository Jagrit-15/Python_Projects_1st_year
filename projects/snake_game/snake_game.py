from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(width = 700 , height = 700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen() # to take commands from the user
screen.tracer(0) # Stops the screen to trace the actions performed by the turtles immediately

snake = Snake()
food = Food()
score = Scoreboard()
game_over = False
speed = 0.1

while not game_over:
    screen.update() # Updates the screen , helps in neglecting the lagging effect
    time.sleep(speed) 
    snake.move()
    screen.onkey(snake.turn_down , "s")
    screen.onkey(snake.turn_left , "a")
    screen.onkey(snake.turn_up , "w")
    screen.onkey(snake.turn_right , "d")

    # Detects if snake eats the food
    if (snake.head.distance(food) < 15):
        food.refresh()
        score.update()
        snake.extend()
    
    # Detects if snake hits the walls
    if snake.isCollision():
        game_over = True
        score.gameOver()

    # Detects if snake hits its own body
    for segment in snake.body:
        if segment == snake.head:
            continue
        elif (snake.head).distance(segment) < 10:
            game_over = True
            score.gameOver()

    # Increasing the speed 
    if score.score == 10:
        speed = 0.08
    elif score.score == 20:
        speed = 0.06
    elif score.score == 30:
        speed = 0.05
screen.exitonclick()