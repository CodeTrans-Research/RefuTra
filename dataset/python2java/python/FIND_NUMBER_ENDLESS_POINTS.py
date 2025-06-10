def f_gold ( input , n ) :
    row = np.zeros ( ( n , n ) )
    col = np.zeros ( ( n , n ) )
    for j in range ( n ) :
        isEndless = 1
        for i in range ( n - 1 , - 1 , - 1 ) :
            if ( input [ i ] [ j ] == 0 ) :
                isEndless = 0
            col [ i ] [ j ] = isEndless
    for i in range ( n ) :
        isEndless = 1
        for j in range ( n - 1 , - 1 , - 1 ) :
            if ( input [ i ] [ j ] == 0 ) :
                isEndless = 0
            row [ i ] [ j ] = isEndless
    ans = 0
    for i in range ( n ) :
        for j in range ( 1 , n ) :
            if ( row [ i ] [ j ] and col [ i ] [ j ] ) :
                ans += 1
    return ans