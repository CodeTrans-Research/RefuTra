public static int f_gold ( int[] a, int n ) {
        Set < Integer > s = new HashSet < > ( );
        for ( int i = 0 ; i < n ; i++ ) s. add ( a [ i ] );
        int sum = 0 ;
        for ( int i : s ) sum += i ;
        return ( 3 * sum - n * ( n + 1 ) / 2 ) ;
    }