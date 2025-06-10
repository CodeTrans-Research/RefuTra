def f_gold ( arr , n ) :
    jumps = [ ]
    i , j = 0 , 0
    if n == 0 or arr [ 0 ] == 0 :
        return int ( 'inf' )
    jumps.append ( 0 )
    for i in range ( 1 , n ) :
        jumps.append ( int ( 'inf' ) )
        for j in range ( i ) :
            if i <= j + arr [ j ] and jumps [ j ] != int ( 'inf' ) :
                jumps [ i ] = min ( jumps [ i ] , jumps [ j ] + 1 )
                break
    return jumps [ n - 1 ]
