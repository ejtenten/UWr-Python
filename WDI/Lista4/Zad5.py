def Ciag(n):
    if n < 3:
        return 1
    a = 1
    b = 1
    c = 1
    temp1 = 0
    temp2 = 0
    licznik = 2
    while licznik != n:
        temp1 = a
        temp2 = b
        a = a + b + c
        b = temp1
        c = temp2
        licznik += 1
    return a

print(Ciag(5))