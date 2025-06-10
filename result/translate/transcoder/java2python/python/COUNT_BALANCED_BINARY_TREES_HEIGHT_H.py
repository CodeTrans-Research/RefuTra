def f_gold ( h ) :
    MOD = 1000000007
    dp = [ 1 ] * h + [ 1 ] * h
    for i in range ( 2 , h + 1 ) :
        dp [ i ] = ( dp [ i - 1 ] * ( ( 2 * dp [ i - 2 ] ) % MOD + dp [ i - 1 ] ) % MOD ) % MOD
    return dp [ h ]