from turtle import *
zolty = "#FFFF00"
niebieski = "#0000FF"
zielony = "#00CE00"
pomaranczowy = "#FFA500"
czerwony = "#FF0000"

speed(0)
penup()

goto(0, -40)
pendown()
fillcolor(zolty)
begin_fill()
circle(40)
end_fill()

penup()
goto(-3, 38)
left(90)

for i in range (1, 38):


    if i % 4 == 1:
        fillcolor(niebieski)
    elif i % 4 == 2:
        fillcolor(czerwony)
    elif i % 4 == 3:
        fillcolor(pomaranczowy)
    elif i % 4 == 0:
        fillcolor(zielony)

    right(90)
    pendown()
    begin_fill()
    forward(3)
    left(90)
    forward(i * 3)
    left(90)
    forward(6)
    left(90)
    forward(i * 3)
    left(90)
    forward(3)
    print(i)
    left(90)
    end_fill()
    penup()
    right(90)
    forward(6.75)
    left(90)
    right(10)

done()
