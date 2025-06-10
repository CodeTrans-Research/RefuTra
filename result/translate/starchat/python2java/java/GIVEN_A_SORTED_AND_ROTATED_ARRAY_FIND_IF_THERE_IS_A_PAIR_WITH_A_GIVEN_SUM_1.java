public static int f_gold ( int arr [ ], int n, int x ) {
    int i ;
    for ( i = 0;
  i < n ;
  i ++ ) if ( arr [ i ] > arr [ i + 1 ] ) break ;
    int l = ( i + 1 ) % n, r = i, cnt = 0;
    while ( l!= r ) {
        if ( arr [ l ] + arr [ r ] == x ) {
            cnt += 1;
            if ( l == ( r - 1 + n ) % n ) return cnt;
            l = ( l + 1 ) % n;
            r = ( r - 1 + n ) % n;
        }
        else if ( arr [ l ] + arr [ r ] < x ) l = ( l + 1 ) % n;
        else r = ( n + r - 1 ) % n;
    }
    return cnt;
}