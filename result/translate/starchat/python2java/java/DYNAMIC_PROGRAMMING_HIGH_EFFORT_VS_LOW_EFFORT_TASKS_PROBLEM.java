public static int f_gold ( int[] high, int[] low, int n ) {
        if ( n <= 0 ) {
            return 0;
        }
        return Math.max( high[n - 1] + f_gold( high, low, n - 2 ), low[n - 1] + f_gold( high, low, n - 1 ) );
    }