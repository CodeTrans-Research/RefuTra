public static boolean f_gold ( String s1, String s2 ) {
        int n = s1. length ( );
        int m = s2. length ( );
        boolean dp [ ] [ ] = new boolean [ n + 1 ] [ m + 1 ];
        dp [ 0 ] [ 0 ] = true;
        for ( int i = 0; i < n; i ++ ) {
            for ( int j = 0; j < m + 1; j ++ ) {
                if ( dp [ i ] [ j ] ) {
                    if ( ( j < m && s1. charAt ( i ) == s2. charAt ( j ) ) ) {
                        dp [ i + 1 ] [ j + 1 ] = true;
                    }
                    if ( Character. isUpperCase ( s1. charAt ( i ) ) == false ) {
                        dp [ i + 1 ] [ j ] = true;
                    }
                }
            }
        }
        return dp [ n ] [ m ];
    }