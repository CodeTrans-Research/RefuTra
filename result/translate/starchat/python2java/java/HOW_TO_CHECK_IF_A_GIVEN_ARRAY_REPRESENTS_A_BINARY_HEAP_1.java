public static boolean f_gold ( int arr [ ], int n ) {
        for ( int i = 0 ; i < ( n - 2 ) / 2 + 1 ; i++ ) {
            if ( arr [ 2 * i + 1 ] > arr [ i ] ) return false;
            if ( 2 * i + 2 < n && arr [ 2 * i + 2 ] > arr [ i ] ) return false;
        }
        return true;
    }