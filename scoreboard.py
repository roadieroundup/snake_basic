from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Pixel NES", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.show_scoreboard()

    def show_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_scoreboard()
