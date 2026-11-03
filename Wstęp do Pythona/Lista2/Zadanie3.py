from math import sqrt

def kolko(n, przesuniecie):
    r = n / 2
    s = (n - 1) / 2

    for i in range(0, n):
        x = int(r - sqrt(r**2 - (i - s)**2) + 0.5)
        print(' ' * przesuniecie + ' ' * x + '#' * (n - 2 * x) + ' ' * x)

def balwan():
    
    kolko(7, 4)
    kolko(9, 3)
    kolko(15, 0)

balwan()