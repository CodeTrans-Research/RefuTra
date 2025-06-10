def f_gold ( k ) :
    cur = ( k * ( k - 1 ) ) + 1
    sum = 0
    while k :
        sum += cur
        cur += 2
    return sum
