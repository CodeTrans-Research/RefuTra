def f_gold ( strA , strB ) :
    res , i = 0 , 0
    for i in range ( len ( strA ) ) :
        res ^= strA [ i ]
    for i in range ( len ( strB ) ) :
        res ^= strB [ i ]
    return ( chr ( res ) , i )
