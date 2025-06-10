public static int f_gold ( int arr [ ], int n ) {
        int res = 0;
        Map < Integer, Integer > m = new HashMap < > ( );
        for ( int i = 0; i < n; i++ ) {
            int Sum = 0;
            for ( int j = i; j < n; j++ ) {
                Sum += arr [ j ];
                m.put ( Sum, m.getOrDefault ( Sum, 0 ) + 1 );
            }
        }
        for ( int x : m.keySet ( ) ) {
            if ( m.get ( x ) == 1 ) {
                res += x;
            }
        }
        return res;
    }