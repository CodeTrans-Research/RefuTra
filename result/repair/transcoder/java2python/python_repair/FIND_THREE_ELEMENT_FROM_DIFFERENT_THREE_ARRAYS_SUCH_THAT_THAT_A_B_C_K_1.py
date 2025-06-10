def f_gold ( a1 , a2 , a3 , n1 , n2 , n3 , sum ) :
    s = set ( )
    for i in range ( n1 ) :
        s.add ( a1 [ i ] )
    al = [ i for i in range ( n2 ) if i != a2 [ i ] ]
    i=0 
    while i<n2 :
        for j in range ( n3 ) :
            if al.count ( sum - a2 [ i ] - a3 [ j ] ) & al.count ( sum - a2 [ i ] - a3 [ j ] ) != al [ - 1 ] :
                return True
        i += 1
    return False

