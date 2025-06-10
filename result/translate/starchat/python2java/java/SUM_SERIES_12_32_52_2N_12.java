public static long f_gold ( long n ) {
        long sum = 0;
        for ( long i = 1 ; i <= n ; i++ ) {
            sum = sum + ( 2 * i - 1 ) * ( 2 * i - 1 );
        }
        return sum;
    }