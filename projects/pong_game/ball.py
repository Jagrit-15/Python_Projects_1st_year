from turtle import Turtle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()

    def start(self):
        random_angle = [random.randint(35,60) * pow(-1,random.randint(1,2)) , random.randint(120,145) * pow(-1,random.randint(1,2))]
        self.setheading(random.choice(random_angle))

    def bounce_wall(self):
        angle = self.heading()
        self.setheading(360 - angle)

    def bounce_plate(self):
        angle = self.heading()
        variation = random.randint(-10 , 10)
        self.setheading(180 - angle + variation)