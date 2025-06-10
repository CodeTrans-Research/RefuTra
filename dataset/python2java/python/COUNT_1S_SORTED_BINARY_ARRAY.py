def f_gold ( arr , low , high ) :
    if high >= low :
        mid = int ( low + ( high - low ) / 2 )
        if ( ( mid == high or arr [ mid + 1 ] == 0 ) and ( arr [ mid ] == 1 ) ) :
            return mid + 1
        if arr [ mid ] == 1 :
            return f_gold ( arr , ( mid + 1 ) , high )
        return f_gold ( arr , low , mid - 1 )
    return 0