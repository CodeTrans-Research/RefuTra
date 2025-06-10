def f_gold ( seq ) :
    n = len ( seq )
    if n >= 9 :
        return "-1"
    result = [ ]
    count = 1
    i=0 
    while i<n+1 :
        if i == n or seq [ i ] == 'I' :
            j=i-1 
            while j>-2 :
                result.append ( chr ( int ( '0' + count ) ) )
                if j >= 0 and seq [ j ] == 'I' :
                    break
                j -= 1
        i += 1
    return ''.join ( result )

