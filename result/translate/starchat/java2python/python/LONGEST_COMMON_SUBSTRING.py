def f_gold(X, Y, m, n):
        LCStuff = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        result = 0
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    LCStuff[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    LCStuff[i][j] = LCStuff[i - 1][j - 1] + 1
                    result = max(result, LCStuff[i][j])
                else:
                    LCStuff[i][j] = 0
        return result