def f_gold ( N ) :
    if N <= 6 :
        return N
    screen = [ ]
    b = 0
    n = 0
    n=1 
    while n<7 :
        screen.append ( n )
        n += 1
    n=7 
    while n<N+1 :
        screen.append ( max ( 2 * screen [ n - 4 ] , max ( 3 * screen [ n - 5 ] , 4 * screen [ n - 6 ] ) ) )
        n += 1
    return screen [ N - 1 ]

