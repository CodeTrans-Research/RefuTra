public static int f_gold ( int arr [ ], int n ) {
        Map < Integer, Integer > mp = new HashMap < > ( );
        for ( int i = 0 ; i < n ; i ++ ) {
            mp.put ( arr [ i ], mp.getOrDefault ( arr [ i ], 0 ) + 1 );
        }
        for ( int i = 0 ; i < n ; i ++ ) {
            if ( mp.get ( arr [ i ] ) == 1 ) {
                return arr [ i ];
            }
        }
        return - 1;
    }