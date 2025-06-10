public static int f_gold ( int arr [ ], int n, int k ) {
        Map < Integer, Integer > count_map = new HashMap < > ( );
        for ( int i = 0 ; i < n ; i++ ) {
            if ( count_map.containsKey ( arr [ i ] ) ) {
                count_map.put ( arr [ i ], count_map.get ( arr [ i ] ) + 1 ) ;
            } else {
                count_map.put ( arr [ i ], 1 ) ;
            }
        }
        for ( int i = 0 ; i < n ; i++ ) {
            if ( count_map.get ( arr [ i ] ).equals ( k ) ) {
                return arr [ i ] ;
            }
        }
        return - 1 ;
    }