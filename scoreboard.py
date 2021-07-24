from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score/score.txt", "r") as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
            with open("score/score.txt", "w") as file:
                file.write(self.high_score)
        self.score = 0
        self.update_score()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 20, "normal"))
