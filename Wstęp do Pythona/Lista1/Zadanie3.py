def krzyzyk(n):
    for i in range(0, n):
        print(' ' * (n - 1), '*' * n)

    for i in range(0, n):
        print('*' * n * 3)

    for i in range(0, n):
        print(' ' * (n - 1), '*' * n)

    return ''

print(krzyzyk(8))