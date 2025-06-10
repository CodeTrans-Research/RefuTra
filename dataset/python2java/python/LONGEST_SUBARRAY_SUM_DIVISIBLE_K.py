def f_gold ( arr , n , k ) :
    um = { }
    mod_arr = [ 0 for i in range ( n ) ]
    max = 0
    curr_sum = 0
    for i in range ( n ) :
        curr_sum += arr [ i ]
        mod_arr [ i ] = ( ( curr_sum % k ) + k ) % k
    for i in range ( n ) :
        if ( mod_arr [ i ] == 0 ) :
            max = i + 1
        elif ( mod_arr [ i ] in um ) :
            um [ mod_arr [ i ] ] = i
        else :
            if ( max < ( i - um [ mod_arr [ i ] ] ) ) :
                max = i - um [ mod_arr [ i ] ]
    return max