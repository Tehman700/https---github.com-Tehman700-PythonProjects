from turtle import Turtle
import random

class Bar:
    def __init__(self):
        self.all_bars = []

    def create(self):
        number = random.randint(1, 6)
        if number == 6:
            def change_color(turtle_instance):
                R = random.random()
                B = random.random()
                G = random.random()
                turtle_instance.color(R, G, B)
        
            n = Turtle("square")
            n.shapesize(1, 2)
            change_color(n)
            n.penup()
            number = random.randint(-240, 270)
            n.goto(300, number)
            self.all_bars.append(n)
    
    def moving(self):
        for bb in self.all_bars:
            bb.backward(10)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_highscore()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(25, 265)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 20, "normal"))
    
    def increase(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset_score(self):
        self.score = 0
        self.update_scoreboard()
    
    def load_highscore(self):
        try:
            with open("texting.txt", mode="r") as file:
                highscore = int(file.readline().strip())
        except (FileNotFoundError, ValueError):
            highscore = 0
        return highscore
    
    def save_highscore(self, highscore):
        with open("texting.txt", mode="w") as file:
            file.write(f"{highscore}\n")
    
    def check_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore(self.highscore)
        self.update_scoreboard()


        
