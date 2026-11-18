from random import randint

def randperm(n):
    if n == 0:
        return 0
    lista = []
    for _ in range(n):
        lista.append(_)

    for i in range(n):
        losowa = randint(0, n - 1)
        element = lista[losowa]
        element1 = lista[i]

        lista[i] = element
        lista[losowa] = element1

    return lista
    

print(randperm(10 ** 6))