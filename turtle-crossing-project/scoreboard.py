from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        pass
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
        pass

    def increase_level(self):
        self.level += 1
        self.update_level()
        pass

    pass
