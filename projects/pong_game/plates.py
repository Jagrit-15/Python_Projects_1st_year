from turtle import Turtle
class Plate(Turtle):

    def __init__(self , player_number: int):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color("white")
        self.penup()
        self.setheading(90)
        if(player_number == 1):
            self.goto(-440 , 0)
        elif(player_number == 2):
            self.goto(430 ,0)

    def up(self):
        self.forward(20)
    def down(self):
        self.backward(20)