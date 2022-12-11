from turtle import Turtle,Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5 , stretch_wid= 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.color("green")
        self.shapesize(stretch_len = 0.5 , stretch_wid= 0.5)
        x_value = random.randint(-260,260)
        y_value = random.randint(-260,260)
        self.goto(x_value,y_value)


