from statistics import mean, median

def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def energia(n):
    licznik = 0

    while n != 1:
        n = F(n) 
        licznik += 1
    return licznik 

def analiza_collatza(a, b):
    energie = {}

    for i in range(a, b + 1):
        energie[i] = energia(i)

    srednia = mean(energie.values())
    mediana = median(energie.values())
    minimum = min(energie.values())
    maksimum = max(energie.values())
    
    return(energie, srednia, mediana, minimum, maksimum)

print(analiza_collatza(6, 8))

