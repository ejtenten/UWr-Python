from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
    pozostale_znaki = n
    haslo = ''


    while (len(haslo) < n - 5):
        wylosowano = losuj_fragment()
        haslo += wylosowano
        pozostale_znaki -= int(len(wylosowano))



    wylosowano = losuj_fragment()

    if pozostale_znaki == 5:
        while len(wylosowano) != 3:
            wylosowano = losuj_fragment()
        haslo += wylosowano
        while len(wylosowano) != 2:
            wylosowano = losuj_fragment()
        haslo += wylosowano


    elif pozostale_znaki == 4:
        while len(wylosowano) != 4:
            wylosowano = losuj_fragment()
        haslo += wylosowano


    elif pozostale_znaki == 3:
            while len(wylosowano) != 3:
                wylosowano = losuj_fragment()
            haslo += wylosowano


    if pozostale_znaki == 2:
            while len(wylosowano) != 2:
                wylosowano = losuj_fragment()
            haslo += wylosowano

    #return n, haslo, len(haslo)
    return haslo



for i in range (0, 10):
     print(losuj_haslo(8))

for i in range (0, 10):
     print(losuj_haslo(12))