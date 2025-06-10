def f_gold ( arr , n ) :
    jumps = [ ]
    min = None
    jumps.append ( n - 1 )
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] == 0 :
            jumps.append ( sys.maxsize)
        elif arr [ i ] >= n - i - 1 :
            jumps.append ( 1 )
        else :
            min = sys.maxsize
            j=i+1 
            while j<n and j<=arr[i]+i :
                if min > jumps [ j ] :
                    min = jumps [ j ]
                j += 1
            if min!=sys.maxsize:
                jumps.append ( min + 1 )
            else :
                jumps.append ( min )
    return jumps [ 0 ]

