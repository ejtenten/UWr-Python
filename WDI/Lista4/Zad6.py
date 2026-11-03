def fTrec(n: int, m: int):
    print(f'Wywołano: {n} - {m}')
    if m == 0:
        return n
    if n == 0:
        return m
    return fTrec(n - 1, m) + 2 * fTrec(n, m - 1)

print(fTrec(3, 4))
