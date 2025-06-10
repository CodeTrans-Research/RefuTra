public static int f_gold ( int n ) {
        n = ( n & ( n + 1 ) ) ^ ( n >> 1 );
        n = ( n & ( n + 1 ) ) ^ ( n >> 2 );
        n = ( n & ( n + 1 ) ) ^ ( n >> 4 );
        n = ( n & ( n + 1 ) ) ^ ( n >> 8 );
        n = ( n & ( n + 1 ) ) ^ ( n >> 16 );
        return n + 1;
    }