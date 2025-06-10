def f_gold(symb, oper, n):
        F = [[0 for _ in range(n)] for _ in range(n)]
        T = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            F[i][i] = (symb[i] == 'F') * 1
            T[i][i] = (symb[i] == 'T') * 1
        for gap in range(1, n):
            for i in range(0, n - gap):
                j = i + gap
                T[i][j] = F[i][j] = 0
                for g in range(0, gap):
                    k = i + g
                    tik = T[i][k] + F[i][k]
                    tkj = T[k + 1][j] + F[k + 1][j]
                    if oper[k] == '&':
                        T[i][j] += T[i][k] * T[k + 1][j]
                        F[i][j] += (tik * tkj - T[i][k] * T