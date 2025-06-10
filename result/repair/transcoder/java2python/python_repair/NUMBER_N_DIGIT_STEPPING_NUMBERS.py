def f_gold ( n ) :
    dp = [[0 for _ in range(10)] for _ in range(n+1)]
    if n == 1 :
        return 10
    j=0 
    while j<10 :
        dp [ 1 ] [ j ] = 1
        j += 1
    for i in range ( 2 , n + 1 ) :
        j=0 
        while j<10 :
            if j == 0 :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ]
            elif j == 9 :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ]
            j += 1
    sum = 0
    j=1 
    while j<10 :
        sum += dp [ n ] [ j ]
        j += 1
    return sum

