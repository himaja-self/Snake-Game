from turtle import Turtle
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font = FONT)

