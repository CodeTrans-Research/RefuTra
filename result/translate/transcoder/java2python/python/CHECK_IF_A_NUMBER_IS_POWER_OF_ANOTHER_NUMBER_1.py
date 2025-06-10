def f_gold ( x , y ) :
    res1 = int ( np.log ( y ) / np.log ( x ) )
    res2 = np.log ( y ) / np.log ( x )
    return ( res1 == res2 )