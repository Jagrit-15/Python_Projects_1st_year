from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,310)
        self.color("white")
        with open("projects/snake_game/high_score.txt") as hs:
            self.high = int(hs.read())
        self.write(f"Score : {self.score} | Highest : {self.high}" , align="center" , font=("Arial" , 24 , "normal"))
        

    def update(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score} | Highest : {self.high}" , align="center" , font=("Arial" , 24 , "normal"))

    def gameOver(self):
        
        if self.score > self.high:
            with open("projects/snake_game/high_score.txt" , mode="w") as hs:
                hs.write(f"{self.score}")
                self.high = self.score
                self.clear()
                self.write(f"Score : {self.score} | Highest : {self.high}" , align="center" , font=("Arial" , 24 , "normal"))
        self.goto(0,0)
        self.write("GAME OVER" , align="center" , font=("Arial" , 24 , "normal"))