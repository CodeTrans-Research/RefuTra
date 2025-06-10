def f_gold(n):
        sum = 0
        for i in range(1, n + 1):
            sum += (n // i) * i
        return sum