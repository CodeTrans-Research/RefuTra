def f_gold(mat, row, column):
        print("Diagonal one : ")
        for i in range(row):
            for j in range(column):
                if i == j:
                    print(mat[i][j] * mat[i][j], end=" ")
            print()
        print("Diagonal two : ")
        for i in range(row):
            for j in range(column):
                if i + j == column - 1:
                    print(mat[i][j] * mat[i][j], end=" ")
            print()