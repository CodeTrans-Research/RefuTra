def f_gold ( a , b , n , k ) :
    a = np.array ( a )
    b = np.array ( b )
    a = np.sort ( a , key = lambda x : x [ 0 ] )
    b = np.sort ( b , key = lambda x : x [ 0 ] )
    for i in range ( n ) :
        if a [ i ] + b [ i ] < k :
            return False
    return True