def usun_duplikaty(L):
    pary = []
    for i in range(len(L)):
        pary.append([L[i], i])
        #print(pary)
    pary.sort()
    #print(pary)

    unikalne = []
    for i in range(len(pary)):
        if i == 0 or pary[i][0] != pary[i - 1][0]:
            unikalne.append([pary[i][1], pary[i][0]])
            #print(unikalne)

    unikalne.sort()
    #print(unikalne)
    wynik = []
    for para in unikalne:
        wynik.append(para[1])
    return wynik


print(usun_duplikaty([1, 2, 3, 1, 2, 3, 8, 2, 2, 2, 9, 9, 4]))
