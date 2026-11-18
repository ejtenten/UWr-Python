from random import choice

def randperm(n):
    if n == 0:
        return 0
    lista = []
    lista2 = []
    for _ in range(n):
        lista2.append(_)

    for i in range(n):
        lista.append(choice(lista2))

    return lista
    

print(randperm(10 ** 6))