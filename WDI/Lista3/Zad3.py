def nwd(a, b):
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    return a

def nwdn():
    n = int(input("Podaj liczbę elementów: "))
    dzielnik = int(input("Podaj liczbę: "))

    i = 1
    while i < n:
        a = int(input("Podaj kolejną liczbę: "))
        dzielnik = nwd(dzielnik, a)
        i += 1

    return dzielnik


print(nwdn())

# nwd: O(max(a, b)) - dla (m, 1) wykonuje m - 1 odejmowań.
# nwdn: O(n*M) - górna granica: n - 1 wywołań nwd, każde najwyżej O(M).
# n to liczba elementów, M to największa wartość; zakładamy dodatnie dane.
