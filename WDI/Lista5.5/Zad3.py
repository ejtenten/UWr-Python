# Specyfikacja:
# Wejście: liczba całkowita n, liczba naturalna k
# Wyjście: liczba n w kodzie uzupełnieniowym U2 na k bitach

from wdi import *

def algorytm(n, k):
    if n < 0:
        ujemna = True
        n *= -1
    else:
        ujemna = False

    A = Array(k)

    temp = n
    licznik = 1
    while temp > 0:
        A[k - licznik] = temp % 2
        licznik += 1
        temp = temp // 2

    if ujemna:
        for i in range(1, k + 1):
            if A[k - i] == 1:
                A[k - i] = 0
            else:
                A[k - i] = 1

        for i in range(1, k + 1):
            if A[k - i] == 0:
                A[k - i] = 1
                break
            elif A[k - i] == 1:
                A[k - i] = 0

    wynik = ''
    for i in range(k):
        wynik = wynik + str(A[i])

    return wynik

print(algorytm(6, 6))