public static int f_gold ( int arr [ ], int n ) {
        Map < Integer, Integer > um = new HashMap < > ( );
        int longLen = 0;
        for ( int i = 0; i < n; i++ ) {
            int len1 = 0;
            if ( arr [ i - 1 ] >= 0 && um.containsKey ( arr [ i - 1 ] ) && len1 < um.get ( arr [ i - 1 ] ) ) {
                len1 = um.get ( arr [ i - 1 ] );
            }
            if ( arr [ i ] + 1 >= 0 && um.containsKey ( arr [ i ] + 1 ) && len1 < um.get ( arr [ i ] + 1 ) ) {
                len1 = um.get ( arr [ i ] + 1 );
            }
            um.put ( arr [ i ], len1 + 1 );
            if ( longLen < um.get ( arr [ i ] ) ) {
                longLen = um.get ( arr [ i ] );
            }
        }
        return longLen;
    }