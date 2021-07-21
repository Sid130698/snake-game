from turtle import Turtle




class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        #self.hideturtle()
    def update_scoreboard(self):
        self.write("Current_ Score ={}".format(self.score),False,align='center')

    def score_update(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,"center")