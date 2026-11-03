def cyfrowa(n):
    if n == 0:
        print(1)
        return

    k = 0
    cyfra = 0
    while cyfra < 10:
        kopia = n

        while kopia > 0 and kopia % 10 != cyfra:
            kopia = kopia // 10

        if kopia > 0:
            k += 1
        cyfra += 1

    print(k)


cyfrowa(1233378)

# O(d), gdzie d to liczba cyfr - 10 razy przeglądamy cyfry liczby.
# O(10*d) = O(d); dla n >= 2 otrzymujemy O(log n).
# Zakładamy stały koszt działań arytmetycznych; dla n = 0: O(1).
