from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.pen()
        self.goto(0, 265)
        self.color("white")
        self.write(f"Score: {self.score}", align='center', font=("Arial", 24, "normal"))
        self.hideturtle()


    def update_scorboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=("Arial", 24, "normal"))


    def reset(self):
        if self.score >self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scorboard()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("Game Over...!", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scorboard()

