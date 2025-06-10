public static int f_gold ( int arr [ ] : int n ) {
        Set < Integer > s = new HashSet < > ( );
        for ( int i = 0; i < n; i++ ) {
            if ( s.contains ( arr [ i ] ) ) return arr [ i ];
            s.add ( arr [ i ] );
        }
        return - 1;
    }