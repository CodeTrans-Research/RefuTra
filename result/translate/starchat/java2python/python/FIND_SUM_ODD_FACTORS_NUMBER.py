def f_gold(n):
        res = 1
        while n % 2 == 0:
            n /= 2
        for i in range(3, int(n**0.5) + 1):
            if n % i == 0:
                count = 0
                while n % i == 0:
                    count += 1
                    n /= i
                res *= (1 + count) * i
        if n > 1:
            res *= (1 + n)
        return res