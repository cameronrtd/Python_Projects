from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.up()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=("Courier", 50, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()