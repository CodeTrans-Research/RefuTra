def f_gold ( a , n ) :
    total = 1
    for i in range ( 2 , ( n + 1 ) + 1 ) :
        total += i
        total -= a [ i - 2 ]
    return total
