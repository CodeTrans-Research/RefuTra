def f_gold(mat, n):
        diag1_left, diag1_right, diag2_left, diag2_right = 0, 0, 0, 0
        for i in range(n):
            if i < n // 2:
                diag1_left += mat[i][i]
                diag2_left += mat[j][i]
            else:
                diag1_right += mat[i][i]
                diag2_right += mat[j][i]
        return (diag1_left == diag2_right and diag2_right == diag2_left and diag1_right == diag2_left and diag2_right == mat[n // 2][n // 2])