def f_gold ( seq ) :
    n = len ( seq )
    if n >= 9 :
        return "-1"
    result = [ ]
    count = 1
    for i in range ( 0 , n ) :
        if i == n or seq [ i ] == 'I' :
            for j in range ( i - 1 , - 1 , - 1 ) :
                result.append ( chr ( int ( '0' + count ) ) )
                if j >= 0 and seq [ j ] == 'I' :
                    break
    return ''.join ( result )
