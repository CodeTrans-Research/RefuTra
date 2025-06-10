def f_gold(M, n, m):
        count = 0
        i, j = 0, m - 1
        while i < n and j >= 0:
            if M[i][j] < 0:
                count += j + 1
                i += 1
            else:
                j -= 1
        return count