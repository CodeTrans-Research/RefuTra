def f_gold ( str ) :
    n = len ( str )
    oddDigSum = 0
    evenDigSum = 0
    for i in range ( 0 , n ) :
        if ( i % 2 == 0 ) :
            oddDigSum = oddDigSum + ( ord ( str [ i ] ) - 48 )
        else :
            evenDigSum = evenDigSum + ( ord ( str [ i ] ) - 48 )
    return ( ( oddDigSum - evenDigSum ) % 11 == 0 )