from turtle import Turtle

MOVE_DISTANCE = 20
MAX_Y_POSITION = 240
MIN_Y_POSITION = -240

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)
        
    def go_up(self):
        if self.ycor() < MAX_Y_POSITION:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > MIN_Y_POSITION:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
        
        


