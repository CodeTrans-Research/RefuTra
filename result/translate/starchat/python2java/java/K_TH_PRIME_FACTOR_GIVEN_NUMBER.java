public static int f_gold ( int n, int k ) {
        while ( n % 2 == 0 ) {
            k--;
            n /= 2;
            if ( k == 0 ) return 2;
        }
        int i = 3;
        while ( i <= (int) Math.sqrt(n) ) {
            while ( n % i == 0 ) {
                if ( k == 1 ) return i;
                k--;
                n /= i;
            }
            i += 2;
        }
        if ( n > 2 && k == 1 ) return n;
        return -1;
    }