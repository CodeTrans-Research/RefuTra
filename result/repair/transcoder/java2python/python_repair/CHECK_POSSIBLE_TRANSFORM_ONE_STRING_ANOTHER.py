def f_gold ( s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , m + 1 ) :
            dp [ i ] [ j ] = False
    dp [ 0 ] [ 0 ] = True
    for i in range ( 0 , len ( s1 ) ) :
        j=0 
        while j<len(s2)+1 :
            if dp [ i ] [ j ] :
                if j < len ( s2 ) and ( ord ( s1 [ i ] ) == ord ( s2 [ j ] ) ) :
                    dp [ i + 1 ] [ j + 1 ] = True
                if not ord ( s1 [ i ] ) :
                    dp [ i + 1 ] [ j ] = True
            j += 1
    return ( dp [ n ] [ m ] )

