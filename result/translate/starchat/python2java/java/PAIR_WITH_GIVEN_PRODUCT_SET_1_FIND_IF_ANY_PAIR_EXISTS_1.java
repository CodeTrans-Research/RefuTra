public static boolean f_gold ( int arr [ ] : int n, int x ) {
        if ( n < 2 ) return false;
        Set < Integer > s = new HashSet < > ( );
        for ( int i = 0 ; i < n ; i ++ ) {
            if ( arr [ i ] == 0 ) {
                if ( x == 0 ) return true;
                else continue;
            }
            if ( x % arr [ i ] == 0 ) {
                if ( x / arr [ i ] in s ) return true;
                s.add ( arr [ i ] );
            }
        }
        return false;
    }