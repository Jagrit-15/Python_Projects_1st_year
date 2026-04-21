from turtle import Turtle , Screen
starting_position = [(0,0) , (-20,0) , (-40,0)] # Each turtle is 20 pixels wide

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in starting_position :
            self.add_segment(position)

    # Adds a segment to the snake's body
    def add_segment(self,position):
        new_body = Turtle("square")
        new_body.penup()
        new_body.color("white")
        new_body.goto(position)
        self.body.append(new_body)

    def extend(self):
        self.add_segment(self.body[-1].position())

    # Movement control of the snake by the user

    def turn_left(self):
        if self.head.heading() != 0: # If the head is pointing at right it cant go left
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180: # If the head is pointing at left it cant go right
            self.head.setheading(0)

    def turn_up(self):
        if self.head.heading() != 270: # If the head is pointing at down it cant go up
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90: # If the head is pointing at up it cant go down
            self.head.setheading(270)

    def move(self):
        # Moving the snake , letting its body follow its head by storing the coordinates of the previous segment of the body
        for segment in range(len(self.body)-1 , 0 , -1): #start stop step
            new_x = self.body[segment-1].xcor()
            new_y = self.body[segment-1].ycor()
            self.body[segment].goto(new_x,new_y)

        # Moving the head after the whole body is completely shifted using the loop
        self.head.forward(20)
        
    def isCollision(self):
        if self.head.xcor() > 345 or self.head.xcor() < -345 or self.head.ycor() > 345 or self.head.ycor() < -345:
            return True