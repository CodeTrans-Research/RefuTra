public static int f_gold( int a, int b ) {
        int count = 0, p = Math.abs( a * b );
        if ( p == 0 ) return 1;
        while ( p > 0 ) {
            count++;
            p /= 10;
        }
        return count;
    }