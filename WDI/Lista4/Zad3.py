def silniowa2(n):
    k = 1
    silnia = 1

    while silnia * (k + 1) <= n:
        k += 1
        silnia *= k

    while k != 0:
        liczba = n // silnia
        print(liczba)

        n = n % silnia
        silnia = silnia // k
        k -= 1

silniowa2(99)
