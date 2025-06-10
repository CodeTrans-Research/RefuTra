def f_gold ( x , y , z ) :
    if ( not int ( y / x )  ) :
        return y if ( not int ( y / z ) ) else z
    return x if ( not int ( x / z )  ) else z