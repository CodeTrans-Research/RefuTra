def f_gold(n, x):
    f_gold = 0
    for i in range(1, min(n, x) + 1):
        if x // i <= n and x % i == 0:
            f_gold += 1
    return f_gold