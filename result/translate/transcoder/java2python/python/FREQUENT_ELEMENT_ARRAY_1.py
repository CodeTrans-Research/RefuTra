def f_gold ( arr , n ) :
    hp = { }
    for i in range ( n ) :
        key = arr [ i ]
        if hp.has_key ( key ) :
            freq = hp [ key ]
            freq += 1
            hp [ key ] = freq
        else :
            hp [ key ] = 1
    max_count , res = - 1 , 0
    for val , count in hp.items ( ) :
        if max_count < count :
            res = val
            max_count = count
    return res