def f_gold(n, r, p):
        C = [0] * (r + 1)
        for i in range(r + 1):
            C[i] = 1
        for i in range(1, n + 1):
            for j in range(min(i, r)):
                C[j] = (C[j] + C[(j - 1) % r]) % p
        return C[r]