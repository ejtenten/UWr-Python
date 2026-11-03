import math

def silnia(i):
    x = math.factorial(i)
    y = int(len(str(x)))
    if y == 1:
        odmiana = 'cyfre'
    elif str(y)[-1] in ['2', '3', '4'] and y not in [12, 13, 14]:
        odmiana = 'cyfry'
    else:
        odmiana = 'cyfr'

    return f'{i}! ma {y} {odmiana}'


for i in range(1, 101):
    print(silnia(i))