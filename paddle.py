from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(position)

    def up(self):
        self.setheading(UP)
        self.forward(40)

    def down(self):
        self.setheading(DOWN)
        self.forward(40)






