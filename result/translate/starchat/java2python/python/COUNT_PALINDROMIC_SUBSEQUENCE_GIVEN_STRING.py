def f_gold(str):
        N = len(str)
        cps = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            cps[i][i] = 1
        for L in range(2, N + 1):
            for i in range(N):
                k = i + L - 1
                if k < N:
                    if str[i] == str[k]:
                        cps[i][k] = cps[i][k - 1] + cps[i + 1][k] + 1
                    else:
                        cps[i][k] = max(cps[i][k - 1], cps[i + 1][k]) + cps[i + 1][k - 1]
        return cps[0][N - 1]