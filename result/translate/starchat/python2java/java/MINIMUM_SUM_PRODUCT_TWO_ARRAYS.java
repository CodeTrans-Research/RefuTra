public static int f_gold ( int[] a, int[] b, int n, int k ) {
        int diff = 0, res = 0, temp = 0;
        for ( int i = 0; i < n; i++ ) {
            int pro = a [ i ] * b [ i ];
            res += pro;
            if ( pro < 0 && b [ i ] < 0 ) {
                temp = ( a [ i ] + 2 * k ) * b [ i ];
            } else if ( pro < 0 && a [ i ] < 0 ) {
                temp = ( a [ i ] - 2 * k ) * b [ i ];
            } else if ( pro > 0 && a [ i ] < 0 ) {
                temp = ( a [ i ] + 2 * k ) * b [ i ];
            } else if ( pro > 0 && a [ i ] > 0 ) {
                temp = ( a [ i ] - 2 * k ) * b [ i ];
            }
            int d = Math.abs ( pro - temp );
            if ( d > diff ) {
                diff = d;
            }
        }
        return res - diff;
    }