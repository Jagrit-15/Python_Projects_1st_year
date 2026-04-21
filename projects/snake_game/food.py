from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(0.5,0.5) # compresses the size of the shape to half of its value 
        self.refresh()
        
    def refresh(self):
        x = random.randint(-320 , 320)
        y = random.randint(-320 , 320)
        self.goto(x,y)