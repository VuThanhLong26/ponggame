from turtle import Screen, Turtle
from padde import Padde
from ball import Ball
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Padde((350, 0))
l_paddle = Padde((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)#sẽ làm quả bóng di chuyển nhanh hay chậm
    #ta muốn quả bóng càng ngày càng nhanh
    ball.move()
    ball.speed("fastest")
    screen.update()
    #phát hiện tường phía trên
    if ball.ycor() > 280 or ball.ycor() < -280:
        #nó cần bật trở lại
        ball.bounce_y()
        #phát hiện paddle bên phải
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        #khoảng cách của ball và paddle và vị trí của quả bóng
        #do paddle dài 100 nên nếu chỉ tính khoảng cách giữa bóng và paddle thì ở 2 cạnh k thể nhận diện được
        ball.bounce_x()
    if ball.xcor() >340:
        #tách riêng để viết thêm mục điểm
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() <-340:
        ball.reset_position()
        scoreboard.r_point()








screen.exitonclick()