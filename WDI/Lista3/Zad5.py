def palindrom(n):
    kopia = n
    odwrocona = 0

    while kopia > 0:
        cyfra = kopia % 2

        odwrocona = odwrocona * 2 + cyfra
        kopia = kopia // 2

    if odwrocona == n:
        return True
    else:
        return False


print(palindrom(67))

# O(log n) dla n >= 2 - każde dzielenie przez 2 usuwa jeden bit.
# Pętla ma floor(log2(n)) + 1 iteracji, każda kosztuje O(1).
# Dla n = 0 i n = 1: O(1).
