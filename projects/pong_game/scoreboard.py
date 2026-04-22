from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self, player_number:int):
        super().__init__()
        self.score = 0
        self.pn = player_number
        self.penup()
        self.hideturtle()
        if player_number == 1:
            self.goto(-225,240)
        elif player_number == 2:
            self.goto(225,240)
        self.color("white")
        self.write(f"Score : {self.score}" , align="center" , font=("Arial" , 24 , "normal"))
        

    def update(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score}" , align="center" , font=("Arial" , 24 , "normal"))

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER :\nPlayer {self.pn} has won\nScore : {self.score}" , align="center" , font=("Arial" , 24 , "normal"))