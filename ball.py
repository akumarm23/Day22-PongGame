from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xm = 10
        self.ym = 10
        self.move_speed = 0.1

    def move(self):
        # Move the ball based on the current speed in x and y directions
        new_x = self.xcor() + self.xm
        new_y = self.ycor() + self.ym
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse the y direction when bouncing off the top or bottom wall
        self.ym *= -1

    def bounce_x(self):
        # Reverse the x direction and slightly increase speed when bouncing off paddles
        self.xm *= -1
        self.move_speed *= 0.9
    
    def rest(self):
        # Reset the ball to the center and bounce in the opposite x direction
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
