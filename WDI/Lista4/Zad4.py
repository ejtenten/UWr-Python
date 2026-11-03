def gcd (n , m ):
    print(f"N: {n}, M: {m}")
    if (m == 0):
        return n
    if (n < m ):
        return gcd (m , n)
    oddcnt = n % 2 + m % 2
    if ( oddcnt == 2):
        return gcd (n -m , m)
    if ( oddcnt == 0):
        return 2 * gcd ( n // 2 , m // 2)
    if (n % 2 == 0):
        return gcd (n // 2 , m)
    else :
        return gcd (n , m // 2)

print(gcd(4, 8))



def gcd2 (n , m ):
    temp = 0
    mnoznik = 1

    while m != 0:
        if (n < m ):
            temp = m
            m = n
            n = temp
        else:
            oddcnt = n % 2 + m % 2
            if oddcnt == 2:
                n -= m
            elif oddcnt == 0:
                mnoznik *= 2
                n = n // 2
                m = m // 2
            elif n % 2 == 0:
                n = n // 2
            else :
                m = m // 2

    return n * mnoznik