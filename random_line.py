from turtle import Turtle,Screen
import random


T=Turtle()
T.shape("turtle")
colours=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
Direction=[0,90,180,270]
T.pensize(10)
T.speed("fastest")

for i in range (300):
    T.color(random.choice(colours))
    T.forward(30)
    T.setheading(random.choice(Direction))

screen=Screen()
screen.exitonclick()
