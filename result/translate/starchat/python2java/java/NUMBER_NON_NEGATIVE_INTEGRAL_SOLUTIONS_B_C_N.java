public static int f_gold ( int n ) {
        int result = 0;
        for ( int i = 0; i <= n; i++ ) {
            for ( int j = 0; j <= n; j++ ) {
                for ( int k = 0; k <= n; k++ ) {
                    if ( i + j + k == n ) {
                        result++;
                    }
                }
            }
        }
        return result;
    }