public static int f_gold ( int n, int x, int y ) {
        boolean [] arr = new boolean [ n + 2 ];
        if ( x <= n ) arr [ x ] = true;
        if ( y <= n ) arr [ y ] = true;
        int result = 0;
        for ( int i = Math.min ( x, y ), n_plus_1 = n + 1; i < n_plus_1; i++ ) {
            if ( arr [ i ] ) {
                if ( i + x <= n ) arr [ i + x ] = true;
                if ( i + y <= n ) arr [ i + y ] = true;
                result++;
            }
        }
        return result;
    }