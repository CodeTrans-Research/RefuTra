public static int f_gold ( int[] A, int[] B, int n ) {
        Arrays.sort ( A );
        Arrays.sort ( B );
        int result = 0;
        for ( int i = 0; i < n; i++ ) {
            result += ( A [ i ] * B [ n - i - 1 ] );
        }
        return result;
    }