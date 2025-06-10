def f_gold ( n , p ) :
    ans = 0 ;
    temp = p ;
    while ( temp <= n ) :
        ans += int(n / temp) ;
        temp = temp * p ;
    return ans ;