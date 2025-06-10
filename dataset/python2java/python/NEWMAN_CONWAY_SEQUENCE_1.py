def f_gold ( n ) :
    f = array.array ( 'i' , [ 0 , 1 , 1 ] )
    for i in range ( 3 , n + 1 ) :
        r = f [ f [ i - 1 ] ] + f [ i - f [ i - 1 ] ]
        f.append ( r )
    return f[n]