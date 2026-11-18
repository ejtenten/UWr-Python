# TO JEST ŹLE ZROBIONE JAK COS
# POTEM NAPRAWIE
from random import randint, choice
from duze_cyfry import *
from turtle import *

bok = 20
ilosc_cyfr = 15
speed(0)

def daj_kolor():
    kolory = [
        (0.00, 0.00, 0.00),  # czarny
        (0.90, 0.00, 0.05),  # czerwony
        (1.00, 0.50, 0.00),  # pomaranczowy
        (0.95, 0.85, 0.00),  # zolty
        (0.00, 0.65, 0.10),  # zielony
        (0.00, 0.80, 0.90),  # cyjan
        (0.10, 0.15, 0.90),  # niebieski
        (0.85, 0.00, 0.75),  # magenta
        (0.55, 0.28, 0.08),  # brazowy
        (0.55, 0.90, 0.00),  # limonkowy
        (0.60, 0.45, 0.85),  # lawendowy
        (0.50, 0.50, 0.50),  # szary
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
        goto(-50, 50)
        setheading(0)
        los1 = randint(0, 1)
        los2 = randint(0, 1)
        if los1 == 1:
            left(90)
        else:
            left(270)
        fd(bok * randint(0, 9))
        if los2 == 1:
            left(90)
        else:
            left(270)
        fd(bok * randint(0, 9))
        pd()
        rysuj(randint(0, 9))

mozaika()
done()
