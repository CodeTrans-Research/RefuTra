def f_gold ( n ) :
    l = int ( math.sqrt ( n ) )
    sq = l * l
    if ( sq == n ) :
        return l * 4
    else :
        row = int ( n / l )
        perimeter = 2 * ( l + row )
        if ( n % l != 0 ) :
            perimeter += 2
        return perimeter