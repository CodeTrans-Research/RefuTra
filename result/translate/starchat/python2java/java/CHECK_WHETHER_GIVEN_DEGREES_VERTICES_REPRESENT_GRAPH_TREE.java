public static boolean f_gold ( int[] degree, int n ) {
        int degSum = 0;
        for ( int i = 0; i < n; i++ ) {
            degSum += degree[i];
        }
        if ( 2 * ( n - 1 ) == degSum ) {
            return true;
        } else {
            return false;
        }
    }