def f_gold ( str ) :
    arr = [ ( '@' , - 1 ) ]
    maxlen = 0
    for i in range ( len ( str ) ) :
        arr.append ( ( str [ i ] , i ) )
        while len ( arr ) >= 3 and arr [ - 3 ] [ 0 ] == '1' and arr [ - 2 ] [ 0 ] == '0' and arr [ - 1 ] [ 0 ] == '0' :
            arr.pop ( - 3 )
            arr.pop ( - 2 )
            arr.pop ( - 1 )
        tmp = arr [ - 1 ] [ 1 ]
        maxlen = max ( maxlen , i - tmp )
    return maxlen