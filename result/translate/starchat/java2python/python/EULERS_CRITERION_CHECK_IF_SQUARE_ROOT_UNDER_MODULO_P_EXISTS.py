def f_gold(n, p):
        n = n % p
        for x in range(2, p):
            if ((x * x) % p == n):
                return True
        return False