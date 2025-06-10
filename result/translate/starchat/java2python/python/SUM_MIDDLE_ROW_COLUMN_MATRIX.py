def f_gold ( mat : List [ List [ int ] ], n ) :
        row_sum = sum ( mat [ n // 2 ] )
        col_sum = sum ( [mat[i][n//2] for i in range ( n )] )
        print ( "Sum of middle row = ", row_sum )
        print ( "Sum of middle column = ", col_sum )