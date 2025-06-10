def f_gold ( arr , n ) :
    jumps = [ ]
    min = None
    jumps.append ( n - 1 )
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] == 0 :
            jumps.append ( int ( arr [ i ] ) )
        elif arr [ i ] >= n - i - 1 :
            jumps.append ( 1 )
        else :
            min = int ( arr [ i + 1 ] )
            for j in range ( i + 1 , n and j <= arr [ i ] + i ) :
                if min > jumps [ j ] :
                    min = jumps [ j ]
            if min != int ( arr [ i ] ) :
                jumps.append ( min + 1 )
            else :
                jumps.append ( min )
    return jumps [ 0 ]
