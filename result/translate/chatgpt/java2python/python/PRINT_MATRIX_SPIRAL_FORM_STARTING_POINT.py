def f_gold(mat, r, c):
    i = 0
    a = 0
    b = 2
    
    low_row = 0 if a < 0 else a
    low_column = 0 if b < 0 else b - 1
    high_row = r - 1 if (a + 1) >= r else a + 1
    high_column = c - 1 if (b + 1) >= c else b + 1
    
    while low_row > 0 - r and low_column > 0 - c:
        for i in range(low_column + 1, high_column + 1):
            if i < c and low_row >= 0:
                print(mat[low_row][i], end=" ")
        low_row -= 1
        
        for i in range(low_row + 2, high_row + 1):
            if i < r and high_column < c:
                print(mat[i][high_column], end=" ")
        high_column += 1
        
        for i in range(high_column - 2, low_column - 1, -1):
            if i >= 0 and high_row < r:
                print(mat[high_row][i], end=" ")
        high_row += 1
        
        for i in range(high_row-2, low_row, -1):
            if i >= 0 and low_column >= 0:
                print(mat[i][low_column], end=" ")
        low_column -= 1
        
    print()