def f_gold ( arr , N , k ) :
    S = 0
    S1 = 0
    max_difference = 0
    for i in range ( N ) :
        S += arr [ i ]
    arr.sort ( reverse = True )
    M = max ( k , N - k )
    for i in range ( M ) :
        S1 += arr [ i ]
    max_difference = S1 - ( S - S1 )
    return max_difference