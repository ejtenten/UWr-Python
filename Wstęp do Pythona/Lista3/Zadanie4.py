from math import sin
from turtle import *

showturtle()
setheading(90)
speed(0)
penup()

goto(-300, 0)
pendown()

i = 0
while xcor() < 310:
    i += 1
    goto(-310 + (i * 5), 0)

    forward(100 * (sin(i / 20)))
    left(90)
    forward(5)
    left(90)
    forward(100 * (sin(i / 20)))
    left(90)
    forward(5)
    left(90)

penup()
hideturtle()

done()