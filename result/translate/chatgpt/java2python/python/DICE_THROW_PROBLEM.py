def f_gold(m, n, x):
    table = [[0 for _ in range(x + 1)] for _ in range(n + 1)]
    for j in range(1, m + 1):
        table[1][j] = 1

    for i in range(2, n + 1):
        for j in range(1, x + 1):
            for k in range(1, j):
                if k <= m:
                    table[i][j] += table[i - 1][j - k]
    
    return table[n][x]