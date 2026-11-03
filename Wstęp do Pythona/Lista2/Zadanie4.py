from duze_cyfry import daj_cyfre

znaki = ['', '', '', '', '']

def zwroc_cyfry(x):
    for cyfra in str(x):
        i = 0
        for r in daj_cyfre(int(cyfra)):
            znaki[i] += r + ' '
            i += 1

    for i in znaki:
        print(i)


zwroc_cyfry(12345)