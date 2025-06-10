public static int f_gold ( int A [ ], int B [ ], int m, int n ) {
        int dp [ ] [ ] = new int [ n + 1 ] [ m + 1 ];
        for ( int i = 0 ; i <= n ; i ++ ) {
            for ( int j = 0 ; j <= m ; j ++ ) {
                if ( i == 0 || j == 0 ) {
                    dp [ i ] [ j ] = 0;
                } else {
                    dp [ i ] [ j ] = Math.max ( dp [ i - 1 ] [ j ], dp [ i ] [ j - 1 ] );
                    if ( j - i >= 0 ) {
                        dp [ i ] [ j ] = Math.max ( dp [ i ] [ j ], dp [ i - 1 ] [ j - i ] + A [ j - i ] * B [ i - 1 ] );
                    }
                }
            }
        }
        return dp [ n ] [ m ];
    }