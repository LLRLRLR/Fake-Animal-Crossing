from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-50,275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-150,0)
        self.write(f"GAME OVER. Score:{self.score}", font=FONT)
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()