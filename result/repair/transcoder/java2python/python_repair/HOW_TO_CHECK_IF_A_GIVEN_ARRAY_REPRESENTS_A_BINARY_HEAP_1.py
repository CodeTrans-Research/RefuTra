def f_gold ( arr , n ) :
    i=0 
    while i<(n-2)/2+1 :
        if arr [ 2 * i + 1 ] > arr [ i ] :
            return False
        if 2 * i + 2 < n and arr [ 2 * i + 2 ] > arr [ i ] :
            return False
        i += 1
    return True

