public static boolean f_gold ( int[] a, int n ) {
        Map < Integer, Integer > mp = new HashMap < > ( );
        for ( int i = 0; i < n; i++ ) {
            if ( mp.containsKey ( a [ i ] ) ) {
                mp.put ( a [ i ], mp.get ( a [ i ] ) + 1 );
            } else {
                mp.put ( a [ i ], 1 );
            }
        }
        for ( int x : mp.keySet ( ) ) {
            if ( mp.get ( x ) >= n / 2 ) {
                return true;
            }
        }
        return false;
    }