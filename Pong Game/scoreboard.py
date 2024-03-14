from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        #score u olusturdugumuz kisim
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()


    def update_score(self):#score u guncelledigimiz metod

        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):#sol paddle a score kazandirdigimiz metod
        self.l_score+=1
        self.clear()
        self.update_score()
    def r_point(self):#sag paddle a score kazandirdigimiz metod
        self.r_score+=1
        self.clear()
        self.update_score()
