def f_gold ( arr , low , high ) :
    max = arr [ low ]
    i = 0
    for i in range ( low , high + 1 ) :
        if arr [ i ] > max :
            max = arr [ i ]
    return max
