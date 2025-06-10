public static int f_gold ( int arr [ ], int n, int k ) {
        int max1 = Integer.MIN_VALUE;
        for ( int i = 0; i < n; i++ ) {
            max1 = Math.max ( max1, arr [ i ] );
        }
        int res = 0;
        for ( int i = 0; i < n; i++ ) {
            if ( ( max1 - arr [ i ] ) % k!= 0 ) {
                return -1;
            }
            res += ( max1 - arr [ i ] ) / k;
        }
        return res;
    }