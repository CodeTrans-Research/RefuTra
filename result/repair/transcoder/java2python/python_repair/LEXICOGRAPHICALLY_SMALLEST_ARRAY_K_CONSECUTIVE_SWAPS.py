def f_gold ( arr , n , k ) :
    for i in range ( n - 1 and k > 0 ) :
        pos = i
        for j in range ( i + 1 , n ) :
            if j - i > k :
                break
            if arr [ j ] < arr [ pos ] :
                pos = j
        temp = None
        j=pos 
        while j>i :
            temp = arr [ j ]
            arr [ j ] = arr [ j - 1 ]
            arr [ j - 1 ] = temp
            j -= 1
        k -= pos - i
