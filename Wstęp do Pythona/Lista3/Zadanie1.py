from math import sqrt

def pierwsza(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(sqrt(n)) + 1):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

licznik = 0

for x in range (1, 100001):
    if '777' in str(x) and pierwsza(x):
        licznik += 1
        print(x)
print('Łącznie: ' + str(licznik))