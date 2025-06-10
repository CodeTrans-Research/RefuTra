public static int f_gold ( int x ) {
        int m = 1 ;
        while ( ( x & m )!= 0 ) {
            x = x ^ m ;
            m = m << 1 ;
        }
        return x ^ m ;
    }