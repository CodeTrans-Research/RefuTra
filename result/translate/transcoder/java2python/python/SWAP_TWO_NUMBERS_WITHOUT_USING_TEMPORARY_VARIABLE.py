def f_gold ( xp , yp ) :
    xp = xp [ : , 0 ] ^ yp [ : , 0 ]
    yp = xp [ : , 1 ] ^ yp [ : , 1 ]
    xp = xp [ : , 2 ] ^ yp [ : , 2 ]
