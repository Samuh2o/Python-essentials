from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.user_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.user_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.user_score > self.high_score:
            self.high_score = self.user_score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.user_score = 0
        self.update_scoreboard() 
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=ALIGNMENT)

    def add_score(self):
        self.user_score += 1
        self.update_scoreboard()
        