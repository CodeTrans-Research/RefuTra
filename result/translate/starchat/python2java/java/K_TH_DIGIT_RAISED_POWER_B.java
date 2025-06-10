public static int f_gold ( int a, int b, int k ) {
        int p = 1;
        while ( p <= a && k > 0 ) {
            if ( p % 10 == a / (p / b) ) {
                k--;
                if ( k == 0 ) return a / (p / b);
            }
            p *= 10;
        }
        return 0;
    }