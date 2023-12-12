from turtle import Turtle

# Constants for text alignment and font
ALIGN = "center"
FONT = ("Courier", 80, "bold")

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left = 0
        self.right = 0
        self.update_score()
        
    def update_score(self):
        # Clear previous score and write the updated score
        self.clear()
        self.goto(-100, 200)
        self.write(self.left, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.right, align=ALIGN, font=FONT)
        
    def l_point(self):
        # Increment the left score and update display
        self.left += 1 
        self.update_score()
    
    def r_point(self):
        # Increment the right score and update display
        self.right += 1 
        self.update_score()
