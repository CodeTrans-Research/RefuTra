def f_gold ( X , Y , l , r , k , dp ) :
    if k == 0 :
        return 0
    if l < 0 | r < 0 :
        return int ( 1e9 )
    if dp [ l ] [ r ] [ k ] != - 1 :
        return dp [ l ] [ r ] [ k ]
    cost = ( X [ l ] - 'a' ) ^ ( Y [ r ] - 'a' )
    return dp [ l ] [ r ] [ k ] = min ( min ( cost + f_gold ( X , Y , l - 1 , r - 1 , k - 1 , dp ) , f_gold ( X , Y , l - 1 , r , k , dp ) ) , f_gold ( X , Y , l , r - 1 , k , dp ) )