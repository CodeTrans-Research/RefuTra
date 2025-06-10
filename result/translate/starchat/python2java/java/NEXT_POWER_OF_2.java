public static int f_gold ( int n ) {
        int count = 0 ;
        if ( n == 0 || ( n & ( n - 1 ) ) == 0 ) return n ;
        while ( n!= 0 ) {
            n = n >> 1 ;
            count++ ;
        }
        return 1 << count ;
    }