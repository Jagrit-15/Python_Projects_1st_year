from turtle import Screen
from ball import Ball
from plates import Plate
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 900 , height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen() # to take commands from the user
screen.tracer(0) # Stops the screen to trace the actions performed by the turtles immediately 

ball = Ball()
ball.start() # Setting the ball at a random angle

player_1 = Plate(1) # initialising player 1
player_2 = Plate(2) # initialising player 2

score1 = Scoreboard(1) # initialising score for player 1
score2 = Scoreboard(2) # initialising score for player 2

# MOVEMENT OF THE PLATES
keys_pressed = set() # creating a set for pressed keys
def press(key):
    keys_pressed.add(key) # moves the plate as long as the key is inside the set
def release(key):
    if key in keys_pressed:
        keys_pressed.remove(key) # removes the key from the set

for key in ["w", "s", "i", "k"]:
    screen.onkeypress(lambda k=key: press(k), key) # lamda stores the value of key
    screen.onkeyrelease(lambda k=key: release(k), key) 
    
play = True

while play:
    screen.update()
    time.sleep(0.05)

    if "w" in keys_pressed:
        player_1.up()
    if "s" in keys_pressed:
        player_1.down()
    if "i" in keys_pressed:
        player_2.up()
    if "k" in keys_pressed:
        player_2.down()

    # REFLECTING THE BALL PERFECTLY WHEN IT STRIKES THE WALL
    if(ball.ycor() >= 280 or ball.ycor() <= -280):
        ball.bounce_wall()

    # REFLECTING THE BALL WITH A VARIATION WHEN IT HITS THE PLATE TO MAKE IT LESS PREDICTABLE
    if(ball.distance(player_1)<30 or ball.distance(player_2)<30):
        ball.bounce_plate()

    # UPDATING SCORES
    if ball.xcor() >500:
        score1.update()
        ball.goto(0,0)
        ball.start()
    if ball.xcor() <-500:
        score2.update()
        ball.goto(0,0)
        ball.start()

    # TERMINATING GAME IF THE SCORE IS MORE THAN 5 
    if(score1.score == 5):
        score1.gameOver()
        play = False
    elif(score2.score == 5):
        score2.gameOver()
        play = False

    ball.forward(20) # moving the ball

screen.exitonclick()