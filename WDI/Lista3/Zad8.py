def podobne(a, b):
    cyfra = 0
    while cyfra < 10:
        ile_a = 0
        ile_b = 0
        x = a
        y = b

        while x > 0:
            if x % 10 == cyfra:
                ile_a += 1
            x = x // 10

        while y > 0:
            if y % 10 == cyfra:
                ile_b += 1
            y = y // 10

        if ile_a != ile_b:
            return False
        cyfra += 1
    return True


print(podobne(32331, 33312))

# O(d_a + d_b), gdzie d_a i d_b to liczby cyfr argumentów.
# Najwyżej 10 razy przeglądamy cyfry obu liczb: O(10*(d_a + d_b)) = O(d_a + d_b).
# Zakładamy stały koszt działań arytmetycznych.
