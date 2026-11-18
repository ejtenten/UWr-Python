def palindromy(a, b):
    lista = []
    for i in range(b + 1):
        lista.append(i)

    for i in range(2, b + 1):
        if lista[i] != 0:
            for j in range(i * 2, b + 1, i):
                lista[j] = 0



    return lista


print(palindromy(90, 200))