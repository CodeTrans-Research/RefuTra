def f_gold ( a , n ) :
    a = a [ : n ]
    a.sort (  )
    sum = 0
    flag = False
    len = 0
    i = 0
    while ( i < n - 1 ) :
        if ( ( a [ i ] == a [ i + 1 ] or a [ i ] - a [ i + 1 ] == 1 ) and flag == False ) :
            flag = True
            len = a [ i + 1 ]
            i = i + 1
        elif ( ( a [ i ] == a [ i + 1 ] or a [ i ] - a [ i + 1 ] == 1 ) and flag == True ) :
            sum = sum + a [ i + 1 ] * len
            flag = False
            i = i + 1
        i += 1
    return sum