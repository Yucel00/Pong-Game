import time
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen=Screen() #turtle kutuphanemizin Screen classina screen objesini tanimladik
screen.setup(width=800,height=600)#800 e 600 luk bir ekran yarattik
screen.bgcolor("black") #arkaplanini siyah yaptik
screen.title("Pong Game") #basligini girdik
screen.tracer(0) #her seyimizi olusturduktan sonra updatemetoduyla acicaz
screen.listen() #listen komutumuzu girdik bu sayede tuslarla fonksiyon birlestirebilicez

l_paddle=Paddle((-350,0)) #sol paddle i mizi olusturduk
r_paddle=Paddle((350,0))  #sag paddle i mizi olusturduk
ball=Ball() #topumuzu olusturduk
score=Score() #score tablomuzu olusturduk

screen.onkey(l_paddle.up,"w") #fonksiyonlari tusa atadik
screen.onkey(l_paddle.down,"s")
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")


is_on=True

while is_on:
    screen.update() #animasyonu durdurdugumuz ekranimizi guncelledik
    time.sleep(ball.move_speed)
    ball.move()#topumuzu harekett ettiren komut ball dosyasinin icinden getirdik

    if ball.ycor()>280 or ball.ycor()<-280: #topun ust ve alt uzakligina gore carpip geri donmesini sagladik
        ball.bounce_y()

    if ball.distance(r_paddle)<55 and ball.xcor()>315 or ball.distance(l_paddle)<55 and ball.xcor()<-315:
        #topun paddle lara gore carpip geri donmesini sagladik
        ball.bounce_x()

    if ball.xcor()>380: #topun sol veya sag duvarlara carptiginda score artmasini ve herseyin baslangic noktasina donmesini sagladik
        ball.reset()
        ball.bounce_x()
        l_paddle.goto(-350,0)
        r_paddle.goto(350,0)
        score.l_point()
    if ball.xcor()<-380:
        ball.reset()
        ball.bounce_x()
        l_paddle.goto(-350,0)
        r_paddle.goto(350,0)
        score.r_point()



screen.exitonclick()
