from turtle import Turtle,Screen
import random


T=Turtle()
T.shape("turtle")
colours=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

T.speed("fastest")

size_of_gap=5
for i in range (int(360/size_of_gap)):
    T.color(random.choice(colours))
    T.circle(100)
    T.setheading(T.heading()+size_of_gap)


screen=Screen()
screen.exitonclick()
