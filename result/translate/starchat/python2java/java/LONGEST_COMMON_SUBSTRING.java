public static int f_gold ( char X [ ], char Y [ ], int m, int n ) {
        int LCSuff [ ] [ ] = new int [ m + 1 ] [ n + 1 ];
        int result = 0;
        for ( int i = 0 ; i <= m ; i ++ ) {
            for ( int j = 0 ; j <= n ; j ++ ) {
                if ( i == 0 || j == 0 ) {
                    LCSuff [ i ] [ j ] = 0;
                } else if ( X [ i - 1 ] == Y [ j - 1 ] ) {
                    LCSuff [ i ] [ j ] = LCSuff [ i - 1 ] [ j - 1 ] + 1;
                    result = Math.max ( result, LCSuff [ i ] [ j ] );
                } else {
                    LCSuff [ i ] [ j ] = 0;
                }
            }
        }
        return result;
    }