def f_gold ( n , r , b , g ) :
    fact = (n + 1) * [0]
    for i in range ( 1 , n + 1 ) :
        fact [ i ] = fact [ i - 1 ] + i
    left = n - ( r + g + b )
    sum = 0
    for i in range ( 0 , left + 1 ) :
        for j in range ( 0 , left - i + 1 ) :
            k = left - ( i + j )
            sum =  sum+fact[n]//(fact[i+r]+fact[j+b]+fact[k+g])
    return sum
