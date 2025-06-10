def f_gold(mat, r, c):
        result = 0
        for i in range(r):
            j = 0
            while j < c - 1:
                if mat[i][j + 1] <= mat[i][j]:
                    break
                j += 1
            if j == c - 1:
                result += 1
        for i in range(r):
            j = c - 1
            while j > 0:
                if mat[i][j - 1] <= mat[i][j]:
                    break
                j -= 1
            if c > 1 and j == 0:
                result += 1
        return result