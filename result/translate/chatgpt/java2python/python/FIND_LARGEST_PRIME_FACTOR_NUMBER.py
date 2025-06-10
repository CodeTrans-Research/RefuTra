def f_gold(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1

    i = 3
    while i <= int(n**0.5):
        while n % i == 0:
            maxPrime = i
            n = n // i
        i += 2

    if n > 2:
        maxPrime = n

    return maxPrime