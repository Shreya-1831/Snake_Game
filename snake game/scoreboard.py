from turtle import Turtle
Font = ("courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.sc = 0
        self.maxi = self.sc
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.sc} ", move=False, align="center", font=Font)
        self.hideturtle()
        self.update_sc()

    def update_sc(self):
        self.clear()
        self.write(f"Score: {self.sc} High Score:{self.maxi}", move=False, align="center", font=Font)

    def reset(self):
        if self.sc > self.maxi:
            self.maxi = self.sc
        self.sc = 0
        self.update_sc()

    def add_score(self):
        self.sc += 1
        self.update_sc()
