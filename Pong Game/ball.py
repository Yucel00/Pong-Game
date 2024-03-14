from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        #init metoduyla topu olusturduk
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):#topu hareket ettiren metod

        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)


    def bounce_y(self):#topun y eksenini degistiren metod
        self.y_move*=-1
        self.move_speed*=0.9

    def bounce_x(self):#topun x eksenini degistiren metod
        self.x_move*=-1
        self.move_speed*=0.9

    def reset(self):#topu baslangic konumuna ve degerine getiren metod
        self.goto(0,0)
        self.move_speed=0.1
