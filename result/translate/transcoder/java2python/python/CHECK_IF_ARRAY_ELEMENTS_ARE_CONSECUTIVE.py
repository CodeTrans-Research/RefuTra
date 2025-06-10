def f_gold ( arr , n ) :
    if n < 1 :
        return False
    min = get_min ( arr , n )
    max = get_max ( arr , n )
    if max - min + 1 == n :
        visited = [ ]
        i = 0
        for i in range ( n ) :
            if visited [ arr [ i ] - min ] != False :
                return False
            visited.append ( arr [ i ] - min )
        return True
    return False