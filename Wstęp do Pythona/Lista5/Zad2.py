from turtle import *

pu()
speed(0)
goto(180, -180)
left(90)
pd()


def kwadrat(r, g, b):
    begin_fill()
    for _ in range(4):
        fd(20)
        left(90)
    fd(20)
    fillcolor(r, g, b)
    end_fill()


bok = 18
bok_copy = bok
r, g, b = 1, 0, 1
while bok > 0:
    for _ in range(bok):
        kwadrat(r, g, b)
    left(90)
    fd(20)
    bok -= 1
    g += 1/bok_copy
    b -= 1/bok_copy
done()