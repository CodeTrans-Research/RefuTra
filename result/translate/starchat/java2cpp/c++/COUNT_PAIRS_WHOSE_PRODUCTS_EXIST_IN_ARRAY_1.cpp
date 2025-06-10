int f_gold ( int arr [ ], int n ) {
        int result = 0 ;
        set < int > s;
        for ( int i = 0 ; i < n ; i ++ ) s.insert ( arr [ i ] ) ;
        for ( int i = 0 ; i < n ; i ++ ) {
            for ( int j = i + 1 ; j < n ; j ++ ) {
                int product = arr [ i ] * arr [ j ] ;
                if ( s.find ( product )!= s.end() ) result++ ;
            }
        }
        return result ;
    }