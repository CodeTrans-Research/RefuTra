public static long f_gold ( long[] poly, int n, long x ) {
        long result = poly[0];
        for ( int i = 1; i < n; i++ ) {
            result = result * x + poly[i];
        }
        return result;
    }