def szachownica(n, k):
    for i in range(0, n):
        for x in range(0, k):
            print(f'{' ' * k}{'#' * k}' * n)
        for y in range(0, k):
            print(f'{'#' * k}{' ' * k}' * n)

szachownica(4, 3)