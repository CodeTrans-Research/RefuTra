def f_gold(n):
    k = n
    imin = 1
    ans = 0
    while ( imin <= n ) :
        imax = int ( n / k )
        ans += k * ( imax - imin + 1 )
        imin = imax + 1
        k = int ( n / imin )
    return ans