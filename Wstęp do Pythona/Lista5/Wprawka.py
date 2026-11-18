def algorytm(n):
    lista = []
    for i in range(n + 1):
        lista.append(i)

    for i in range(2, n + 1):
        if lista[i] != 0:
            for j in range(i * 2, n + 1, i):
                lista[j] = 0

    wynik = []
    licznik = 0

    for i in lista:
        if i != 0 and i != 1:
            wynik.append(i)
            licznik += 1

    return wynik, licznik

wypisz_do = 10000
liczby, ilosc = algorytm(wypisz_do)

if wypisz_do <= 100:
    print(f'Liczby: {liczby}')
    print(f'Ile ich: {ilosc}')
else:
    #print(f'Liczby: {liczby}')
    print(f'Ile ich: {ilosc}')
