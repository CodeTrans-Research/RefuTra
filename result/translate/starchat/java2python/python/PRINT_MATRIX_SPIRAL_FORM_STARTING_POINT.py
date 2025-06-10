def f_gold(mat, r, c):
        i, a, b = 0, 0, 2
        low_row = max(0, -a)
        low_column = max(0, -b)
        high_row = min(r, a + 1)
        high_column = min(c, b + 1)
        while low_row > 0 - r and low_column > 0 - c:
            for i in range(low_column + 1, high_column + 1):
                if low_row >= 0:
                    print(mat[low_row][i], end=" ")
            low_row -= 1
            for i in range(low_row + 2, high_row + 1):
                if high_column < c:
                    print(mat[i][high_column], end=" ")
            high_column += 1
            for i in range(high_column - 2, low_column - 1, -1):
                if high_row < r:
                    print(mat[high_row][i], end=" ")
            high_row += 1
            for i in range(high_row - 2, low_row - 1, -1):
                if low_column >= 0:
                    print(mat[i][low_column], end=" ")
            low_column -= 1
        print()