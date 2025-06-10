def f_gold(n):
        C = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            j=0 
            while j<min(i,n)+1 :
                if j == 0 or j == i:
                    C[i][j] = 1
                else:
                    C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
                j += 1
        sum = 0
        for i in range(n + 1):
            sum += C[n][i] * C[n][i]
        return sum
