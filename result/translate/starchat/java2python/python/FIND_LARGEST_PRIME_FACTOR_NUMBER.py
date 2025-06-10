def f_gold(n):
        maxPrime = -1
        while n % 2 == 0:
            maxPrime = 2
            n = n // 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                maxPrime = i
                n = n // i
        if n > 2:
            maxPrime = n
        return maxPrime