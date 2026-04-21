from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,310)
        self.color("white")
        self.write(f"Score : {self.score}" , align="center" , font=("Arial" , 24 , "normal"))
        

    def update(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score}" , align="center" , font=("Arial" , 24 , "normal"))

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER" , align="center" , font=("Arial" , 24 , "normal"))