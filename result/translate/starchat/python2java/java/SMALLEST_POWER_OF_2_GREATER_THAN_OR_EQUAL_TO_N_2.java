public static int f_gold ( int n ) {
        n = ( n & ( n >> 1 ) ) ^ ( n & ( n >> 2 ) );
        n = ( n & ( n >> 4 ) ) ^ ( n & ( n >> 8 ) );
        n = ( n & ( n >> 16 ) ) ^ ( n & ( n >> 32 ) );
        return n + 1;
    }