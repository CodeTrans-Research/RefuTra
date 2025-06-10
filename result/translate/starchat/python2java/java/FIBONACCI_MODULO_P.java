public static int f_gold ( int p ) {
        int first = 1, second = 1, number = 2, next;
        while ( ( next = ( first + second ) % p )!= 0 ) {
            first = second;
            second = next;
            number = number + 1;
        }
        return number;
    }