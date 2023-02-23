from turtle import Turtle, Screen

WIDTH = 5
HEIGHT = 1
X_POSITION = 350
Y_POSITION = 0


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.goto(position)

    def up(self):
        self.goto(self.xcor(),self.pos()[1]+20) 

    def down(self):
        self.goto(self.xcor(),self.pos()[1]-20) 
    pass