public static boolean f_gold ( int n ) {
        int [] ar = new int [ 10 ];
        while ( n > 0 ) {
            int digit = ( n % 10 );
            if ( ar [ digit ] == 1 ) return false;
            ar [ digit ] = 1;
            n /= 10;
        }
        return true;
    }