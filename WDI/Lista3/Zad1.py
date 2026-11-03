def a(n):
    if n % 2 == 0:
        x = 1
    else:
        x = -1
    x *= n
    return x
# a(n): O(1) - stała liczba działań, niezależna od n; nie ma pętli.

def b(n):
    suma = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            x = 1
        else:
            x = -1
        suma += (x / i)
        i += 1
    return suma
# b(n): O(n) - pętla wykonuje n iteracji, każda zajmuje O(1).


def c(n, x):
    suma = 0
    y = x
    i = 1
    while i <= n:
        x = y
        j = 1
        while j < i:
            x *= y
            j += 1
        suma += i * x
        i += 1
    return suma
# c(n, x): O(n^2) - pętle wykonują łącznie n(n - 1)/2 iteracji.



print(c(1, 2))
print(c(2, 2))
print(c(3, 2))
print(c(4, 2))
print(c(5, 2))
print(c(3, 3))

