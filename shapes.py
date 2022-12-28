from turtle import Turtle,Screen
import random

def shape(no):
    for i in range(no):
        angle=360/no
        T.forward(50)
        T.right(angle)

T=Turtle()
T.shape("turtle")
colours=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]


for i in range (3,15):
    T.color(random.choice(colours))
    shape(i)

screen=Screen()
screen.exitonclick()
