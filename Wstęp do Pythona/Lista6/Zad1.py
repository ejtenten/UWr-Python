from random import randint, choice
from duze_cyfry import *
from turtle import *

bok = 20
ilosc_cyfr = 20
speed(0)

def daj_kolor():
    kolory = [
        (0.95, 0.35, 0.40),  # koralowy
        (0.15, 0.75, 0.70),  # turkusowy
        (0.60, 0.40, 0.85),  # fioletowy
        (1.00, 0.75, 0.20),  # zloty
        (0.25, 0.55, 0.95),  # niebieski
        (1.00, 1.00, 0.00),
    ]
    return choice(kolory)

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

def rysuj_linie(linia, kolor):
    pu()
    right(90)
    fd(bok)
    left(90)
    for i in linia:
        if i == '#':
            kwadrat(kolor[0], kolor[1], kolor[2])
        else:
            fd(bok)
    pu()
    left(180)
    fd(bok * 5)
    left(180)

def rysuj(liczba):
    setheading(0)
    liczba = str(liczba)
    kolor = daj_kolor() 
    for linia in daj_cyfre(int(liczba)):
        rysuj_linie(linia, kolor)
    left(90)
    fd(bok * 5)
    right(90)
    fd(bok * 6)

def mozaika():
    for _ in range(ilosc_cyfr):
        pu()
        goto(0, 0)
        los1 = randint(0, 1)
        los2 = randint(0, 1)
        if los1 == 1:
            left(90)
        else:
            left(270)
        fd(bok * randint(0, 7))
        if los2 == 1:
            left(90)
        else:
            left(270)
        fd(bok * randint(0, 7))
        pd()
        left(180)
        rysuj(randint(0, 9))

mozaika()
done()