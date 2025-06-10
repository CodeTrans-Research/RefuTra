def f_gold ( p ) :
    check_number = long ( pow ( 2 , p ) ) - 1
    nextval = 4 % check_number
    for i in range ( 1 , p - 1 ) :
        nextval = ( nextval * nextval - 2 ) % check_number
    return ( nextval == 0 )