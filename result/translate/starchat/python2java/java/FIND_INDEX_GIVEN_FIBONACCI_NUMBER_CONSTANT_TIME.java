public static int f_gold ( int n ) {
        if ( n <= 1 ) return n;
        int a = 0, b = 1, c = 1, res = 1;
        while ( c < n ) {
            c = a + b;
            res = res + 1;
            a = b;
            b = c;
        }
        return res;
    }