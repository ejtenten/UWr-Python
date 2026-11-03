def nww(a, b):
    x = a
    y = b
    while a != b:
        if a > b:
            b += y
        else:
            a += x
    return a


def nwd(a, b):
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    return a

def b(a, b):
    x = nwd(a, b)
    a = int(a / x)
    b = int(b / x)
    return f'{a}/{b}'

print(b(123456, 789012))

# nww: O((a + b)/g), g = NWD(a, b) - pętla ma a/g + b/g - 2 iteracji.
# nwd: O(max(a, b)) - dla (m, 1) wykonuje m - 1 odejmowań.
# b: O(max(a, b)) - dominuje wywołanie nwd; zakładamy a, b > 0.
