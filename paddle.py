from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "purple",
          "orange", "pink", "brown", "cyan", "magenta",
          "teal", "indigo", "maroon", "navy", "olive", 
          "silver", "aqua", "fuchsia", "lime", "gray"]

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.random_color = random.choice(COLORS)
        self.color(self.random_color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        # Move the paddle up by 30 units in the y-direction
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # Move the paddle down by 30 units in the y-direction
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
