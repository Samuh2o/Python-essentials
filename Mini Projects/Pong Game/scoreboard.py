from turtle import Turtle

POINTS_FONT = ('Courier', 80, 'normal')
MESSAGE_FONT = ('Courier', 25, 'normal')
ALIGNMENT = "center"
RIGHT_X_POSITION = 90
LEFT_X_POSITION = -130
Y_POSITION = 190

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.winner = "none"
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(RIGHT_X_POSITION, Y_POSITION)
        self.write(f"{self.r_score}", font=POINTS_FONT)
        self.goto(LEFT_X_POSITION, Y_POSITION)
        self.write(f"{self.l_score}", font=POINTS_FONT)

    def game_over(self):
        self.goto(0,0)
        if self.l_score > self.r_score:
            self.winner = "Left"
        else:
            self.winner = "Right"
        self.write(f"{self.winner} player win!", align=ALIGNMENT, font=MESSAGE_FONT)
