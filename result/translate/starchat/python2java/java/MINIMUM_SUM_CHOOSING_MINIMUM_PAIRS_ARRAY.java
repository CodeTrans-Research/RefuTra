public static int f_gold ( int A [ ] : int n ) {
        int min_val = Integer. MIN_VALUE ;
        for ( int i = 0 ; i < n ; i++ ) {
            if ( A [ i ] < min_val ) min_val = A [ i ] ;
        }
        return min_val * ( n - 1 ) ;
    }