public static int f_gold ( int arr [ ], int n ) {
        int maxv = Integer.MIN_VALUE, minv = Integer.MAX_VALUE;
        for ( int i = 0; i < n; i++ ) {
            maxv = Math.max ( maxv, arr [ i ] );
            minv = Math.min ( minv, arr [ i ] );
        }
        int res = 0, mp [ ] = new int [ maxv - minv + 1 ];
        for ( int i = 0; i < n; i++ ) mp [ arr [ i ] - minv ]++;
        for ( int i = minv; i <= maxv; i++ ) res = Math.max ( res, mp [ i - minv ] );
        return res;
    }