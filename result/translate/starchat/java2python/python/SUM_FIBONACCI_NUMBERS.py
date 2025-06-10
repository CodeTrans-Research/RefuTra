def f_gold(n):
        if n <= 0:
            return 0
        fibo = [0] * (n + 1)
        fibo[0] = 0
        fibo[1] = 1
        for i in range(2, n + 1):
            fibo[i] = fibo[i - 1] + fibo[i - 2]
        sum = fibo[0] + fibo[1]
        return sum