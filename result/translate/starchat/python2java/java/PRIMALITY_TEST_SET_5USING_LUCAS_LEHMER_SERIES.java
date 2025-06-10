public static boolean f_gold ( int p ) {
        long checkNumber = ( long ) ( 1 << p ) - 1;
        long nextval = 4 % checkNumber;
        for ( int i = 1; i < p - 1; i++ ) {
            nextval = ( nextval * nextval - 2 ) % checkNumber;
        }
        if ( nextval == 0 ) {
            return true;
        }
        else {
            return false;
        }
    }