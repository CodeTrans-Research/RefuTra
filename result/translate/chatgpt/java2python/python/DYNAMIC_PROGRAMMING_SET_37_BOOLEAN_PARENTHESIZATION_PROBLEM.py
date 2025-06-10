def f_gold(symb, oper, n):
    F = [[0 for _ in range(n)] for _ in range(n)]
    T = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        F[i][i] = 1 if symb[i] == 'F' else 0
        T[i][i] = 1 if symb[i] == 'T' else 0
    
    for gap in range(1, n):
        for i in range(n-gap):
            j = i + gap
            T[i][j] = F[i][j] = 0
            for g in range(gap):
                k = i + g
                tik = T[i][k] + F[i][k]
                tkj = T[k+1][j] + F[k+1][j]
                if oper[k] == '&':
                    T[i][j] += T[i][k] * T[k+1][j]
                    F[i][j] += (tik * tkj) - (T[i][k] * T[k+1][j])
                elif oper[k] == '|':
                    F[i][j] += F[i][k] * F[k+1][j]
                    T[i][j] += (tik * tkj) - (F[i][k] * F[k+1][j])
                elif oper[k] == '^':
                    T[i][j] += F[i][k] * T[k+1][j] + T[i][k] * F[k+1][j]
                    F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]
    
    return T[0][n-1]