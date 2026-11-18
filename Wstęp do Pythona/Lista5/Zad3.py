from random import random
from duze_cyfry import *
from turtle import *

bok = 20
speed(0)
pu()
goto(-300, 75)
pd()

def kwadrat(r, g, b):
    pd()
    begin_fill()
    for _ in range(4):
        fd(bok)
        left(90)
    fd(bok)
    fillcolor(r, g, b)
    end_fill()
    pu()

def rysuj_linie(linia, r, g, b):
    pu()
    right(90)
    fd(bok)
    left(90)
    for i in linia:
        if i == '#':
            kwadrat(r, g, b)
        else:
            fd(bok)
    pu()
    left(180)
    fd(bok * 5)
    left(180)

def rysuj(liczba):
    liczba = str(liczba)
    licznik = 0
    for i in liczba:
        r, g, b = random(), random(), random()
        print(i)
        for linia in daj_cyfre(int(i)):
            rysuj_linie(linia, r, g, b)
        left(90)
        fd(bok * 5)
        right(90)
        fd(bok * 6)


rysuj(2137)
done()