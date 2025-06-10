def f_gold(M, n, m):
        count = 0
        for i in range(n):
            for j in range(m):
                if M[i][j] < 0:
                    count += 1
                    break
        return count