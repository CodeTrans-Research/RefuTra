int f_gold ( int arr [ ], int n ) {
    set < int > S;
    for ( int i = 0 ; i < n ; i ++ ) S. insert ( arr [ i ] ) ;
    int ans = 0 ;
    for ( int i = 0 ; i < n ; i ++ ) {
        if ( S. find ( arr [ i ] )!= S. end ( ) ) {
            int j = *S. lower_bound ( arr [ i ] ) ;
            while ( S. find ( j )!= S. end ( ) ) j ++ ;
            ans = max ( ans, j - arr [ i ] ) ;
        }
    }
    return ans ;
}