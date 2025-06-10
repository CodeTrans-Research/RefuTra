def f_gold ( pre, n ) :
    s = [ ]
    root = -2147483648
    for i in range(n) :
        if pre[i] < root :
            return False
        while ( len ( s ) > 0 and s [ - 1 ] < pre[i] ) :
            root = s.pop ( )
        s.append ( pre[i] )
    return True