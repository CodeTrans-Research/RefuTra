public static int f_gold ( int n ) {
    int res = 1;
    while ( n % 2 == 0 ) {
        n /= 2;
    }
    for ( int i = 3; i * i <= n; i++ ) {
        int count = 0;
        int curr_sum = 1;
        int curr_term = 1;
        while ( n % i == 0 ) {
            count++;
            n /= i;
            curr_term *= i;
            curr_sum += curr_term;
        }
        res *= curr_sum;
        if ( n == 1 ) {
            break;
        }
    }
    if ( n > 1 ) {
        res *= ( n + 1 );
    }
    return res;
}