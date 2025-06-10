def f_gold ( ar , n ) :
    res = 0
    ar.sort ( )
    i = 0
    while i < n:
        count = 1
        j = i
        while j < n - 1:
            if ar [ j ] == ar [ j + 1 ] :
                count += 1
            else :
                break
            j += 1
        i = j
        i += 1
        res = max ( res , count )
    return res