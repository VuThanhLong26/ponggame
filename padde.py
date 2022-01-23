from turtle import Turtle

class Padde(Turtle):
    def __init__(self, position):

        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        # vì mỗi square có kích thước mặc định là 20*20
        # để tạo ra paddle dài 100 rộng 20
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
