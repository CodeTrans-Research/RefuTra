public static int f_gold ( int n ) {
        int res = 1 ;
        for ( int i = n ; i >= 2 ; i -= 2 ) {
            if ( i == 2 ) {
                return res ;
            }
            res *= i ;
        }
        return res;
    }