def palindromy(a, b):
    lista = []
    for i in range(b + 1):
        lista.append(i)

    for i in range(2, b + 1):
        if lista[i] != 0:
            for j in range(i * 2, b + 1, i):
                lista[j] = 0

    wynik = []
    for i in range(max(a, 2), b + 1):
        liczba = str(i)
        if lista[i] != 0 and liczba == liczba[::-1]:
            wynik.append(i)

    return wynik


print(palindromy(90, 200))