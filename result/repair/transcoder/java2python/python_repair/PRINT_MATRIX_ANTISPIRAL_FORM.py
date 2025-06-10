def f_gold ( m , n , a ) :
    i , k , l = 0 , 0 , 0
    stk = [ ]
    while k <= m and l <= n :
        for i in range ( l , n + 1 ) :
            stk.append ( a [ k ] [ i ] )
        k += 1
        for i in range ( k , m + 1 ) :
            stk.append ( a [ i ] [ n ] )
        n -= 1
        if k <= m :
            i=n 
            while i>l-1 :
                stk.append ( a [ m ] [ i ] )
                i -= 1
            m -= 1
        if l <= n :
            i=m 
            while i>k-1 :
                stk.append ( a [ i ] [ l ] )
                i -= 1
            l += 1
    while not stk :
        print ( stk.pop ( ) , end = ' ' )
        stk.pop ( )
