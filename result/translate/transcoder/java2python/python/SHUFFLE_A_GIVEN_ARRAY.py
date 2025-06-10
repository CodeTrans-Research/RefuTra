def f_gold ( arr , n ) :
    r = random.Random ( )
    for i in range ( n - 1 , 0 , - 1 ) :
        j = r.randint ( i + 1 , i + 1 )
        temp = arr [ i ]
        arr [ i ] = arr [ j ]
        arr [ j ] = temp
    return arr