public static int f_gold ( int arr [ ] arr_size, int n, int x, int y ) {
        int min_dist = 2147483647;
        for ( int i = 0; i < n; i++ ) {
            for ( int j = i + 1; j < n; j++ ) {
                if ( ( x == arr [ i ] && y == arr [ j ] ) || ( y == arr [ i ] && x == arr [ j ] ) ) {
                    min_dist = Math.min ( min_dist, Math.abs ( i - j ) );
                }
            }
        }
        return min_dist;
    }