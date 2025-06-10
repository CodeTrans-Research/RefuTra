public static boolean f_gold ( int a, int b, int c ) {
        if ( ( a + b ) <= c || ( a + c ) <= b || ( b + c ) <= a ) {
            return false;
        }
        return true;
    }