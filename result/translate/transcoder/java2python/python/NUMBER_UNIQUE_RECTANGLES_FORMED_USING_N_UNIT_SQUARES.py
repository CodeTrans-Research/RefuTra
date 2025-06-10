def f_gold ( n ) :
    ans = 0
    for length in range ( 1 , math.sqrt ( n ) + 1 ) :
        for height in range ( length , length * length <= n ) :
            ans += 1
    return ans
