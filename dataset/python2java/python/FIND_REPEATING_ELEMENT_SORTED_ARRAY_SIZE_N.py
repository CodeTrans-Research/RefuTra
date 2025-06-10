def f_gold ( arr , low , high ) :
    if low > high :
        return - 1
    mid = int ( ( low + high ) / 2 )
    if ( arr [ mid ] != mid + 1 ) :
        if ( mid > 0 and arr [ mid ] == arr [ mid - 1 ] ) :
            return mid
        return f_gold ( arr , low , mid - 1 )
    return f_gold ( arr , mid + 1 , high )