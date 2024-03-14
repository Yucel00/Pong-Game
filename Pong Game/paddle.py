from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,positions):
        super().__init__()

        #init fonksiyonuicinde paddle imizi yarattik icine posizsyon girdirerek birden fazla farkli konumda nesne olsuturabiliriz
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(positions)


    def up(self):#paddle i yukari goturme metodu
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def down(self):#paddle i asagi goturme komutu
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)
