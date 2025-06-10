public static int f_gold ( int arr [ ], int n ) {
        Map < Integer, Integer > mp = new HashMap < > ( );
        for ( int i = 0; i < n; i++ ) {
            mp.put ( arr [ i ], mp.getOrDefault ( arr [ i ], 0 ) + 1 );
        }
        int max_count = 0, min_count = n;
        for ( int key : mp.keySet ( ) ) {
            max_count = Math.max ( max_count, mp.get ( key ) );
            min_count = Math.min ( min_count, mp.get ( key ) );
        }
        return max_count - min_count;
    }