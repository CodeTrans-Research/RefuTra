def f_gold ( num ) :
    n = len ( num )
    sumofdigit = [ ]
    sumofdigit.append ( ord ( num [ 0 ] ) - ord('0') )
    res = sumofdigit [ 0 ]
    for i in range ( 1 , n ) :
        numi = ord ( num [ i ] ) - ord ( '0' )
        sumofdigit.append ( ( i + 1 ) + numi + 10 + sumofdigit [ i - 1 ] )
        res += sumofdigit [ i ]
    return res