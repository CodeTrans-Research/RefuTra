def f_gold ( str , l , h ) :
    if l > h :
        return int ( l )
    if l == h :
        return 0
    if l == h - 1 :
        return ( str [ l ] , str [ h ] )
    return ( str [ l ] , str [ h ] ) if f_gold ( str , l + 1 , h - 1 ) else ( min ( f_gold ( str , l , h - 1 ) , f_gold ( str , l + 1 , h ) ) + 1 )
