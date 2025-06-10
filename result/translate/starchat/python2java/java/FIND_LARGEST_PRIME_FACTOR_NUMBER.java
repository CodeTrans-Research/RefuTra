public static int f_gold ( int n ) {
        int maxPrime = -1;
        while ( n % 2 == 0 ) {
            maxPrime = 2;
            n /= 2;
        }
        for ( int i = 3 ; i <= (int) Math.sqrt(n) ; i += 2 ) {
            while ( n % i == 0 ) {
                maxPrime = i;
                n /= i;
            }
        }
        if ( n > 2 ) {
            maxPrime = n;
        }
        return maxPrime;
    }