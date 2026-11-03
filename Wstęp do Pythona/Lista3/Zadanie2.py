from math import sqrt

def pierwsza(n):
    n = int(n)
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(sqrt(n)) + 1):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

ilosc_siodemek = 7
ilosc_liczb = 10

pozostale = ilosc_liczb - ilosc_siodemek
licznik = 0

for i in range(10 ** pozostale):
    for pozycja in range(pozostale + 1):
        potega = 10 ** pozycja
        poczatek = i // potega

        if poczatek % 10 != 7:
            liczba = poczatek
            for j in range(ilosc_siodemek):
                liczba = liczba * 10 + 7

            liczba = liczba * potega + i % potega

            if liczba >= 10 ** (ilosc_liczb - 1) and pierwsza(liczba):
                licznik += 1
                print(liczba)

print('Łącznie: ' + str(licznik))
