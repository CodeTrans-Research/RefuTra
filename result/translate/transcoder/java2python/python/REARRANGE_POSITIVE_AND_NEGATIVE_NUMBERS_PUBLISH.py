def f_gold ( arr , n ) :
    i , temp = - 1 , 0
    for j in range ( n ) :
        if arr [ j ] < 0 :
            i += 1
            temp = arr [ i ]
            arr [ i ] , arr [ j ] = arr [ j ] , temp
    pos , neg = i + 1 , 0
    while pos < n and neg < pos and arr [ neg ] < 0 :
        temp = arr [ neg ]
        arr [ neg ] , arr [ pos ] = arr [ pos ] , temp
        pos += 1
        neg += 2
    return arr , temp
