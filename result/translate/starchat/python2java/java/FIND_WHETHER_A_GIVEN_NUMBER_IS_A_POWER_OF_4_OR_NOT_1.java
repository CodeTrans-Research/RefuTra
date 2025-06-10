public static boolean f_gold ( int n ) {
        if ( ( n & ( n - 1 ) ) == 0 ) {
            return ( n > 1 )? true : false;
        }
        return false;
    }