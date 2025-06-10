public static boolean f_gold ( int n ) {
        while ( n / 100 > 0 ) {
            int lastDigit = n % 10;
            n /= 10;
            n += last_digit * 3;
        }
        return ( n % 29 == 0 );
    }