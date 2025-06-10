def f_gold(m, n, x):
        table = [[0 for i in range(x + 1)] for j in range(n + 1)]
        for j in range(1, min(m, x) + 1):
            table[1][j] = 1
        for i in range(2, n + 1):
            for j in range(1, x + 1):
                for k in range(1, min(j, i) + 1):
                    table[i][j] += table[i - 1][j - k]
        return table[n][x]