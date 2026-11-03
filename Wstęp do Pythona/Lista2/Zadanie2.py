def koperta(n):
    x = 2 * n + 1
    print('*' * x)

    for i in range(0, int((x - 2) / 2)):
        print('*' + ' ' * i + '*' + ' ' * ((x - 4) - 2 * i) + '*' + ' ' * i + '*')

    print('*' + ' ' * int((x - 2) / 2) + '*' + ' ' * int((x - 2) / 2) + '*')

    j = int((x - 2) / 2) - 1
    while j >= 0:
        print('*' + ' ' * j + '*' + ' ' * ((x - 4) - 2 * j) + '*' + ' ' * j + '*')
        j -= 1

    print('*' * x)

koperta(6)