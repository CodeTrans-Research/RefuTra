def f_gold ( XY , n , Xmin , Ymin , Xmax , Ymax ) :
    print ( "Point inside the viewing pane:" )
    for i in range ( n ) :
        if ( XY [ i ] [ 0 ] >= Xmin ) :
            if ( XY [ i ] [ 0 ] <= Xmax ) :
                if ( XY [ i ] [ 1 ] >= Ymin ) :
                    print ( "[%d, %d] " % ( XY [ i ] [ 0 ] , XY [ i ] [ 1 ] ) )
    print ( "\nPoint outside the viewing pane:" )
    for i in range ( n ) :
        if ( XY [ i ] [ 0 ] < Xmin ) :
            if ( XY [ i ] [ 0 ] > Xmax ) :
                print ( "[%d, %d] " % ( XY [ i ] [ 0 ] , XY [ i ] [ 1 ] ) )
            if ( XY [ i ] [ 1 ] < Ymin ) :
                if ( XY [ i ] [ 1 ] > Ymax ) :
                    print ( "[%d, %d] " % ( XY [ i ] [ 0 ] , XY [ i ] [ 1 ] ) )