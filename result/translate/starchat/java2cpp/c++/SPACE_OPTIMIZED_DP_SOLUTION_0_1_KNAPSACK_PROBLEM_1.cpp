int f_gold ( int val [ ], int wt [ ], int n, int W ) {
  int *dp = new int [ W + 1 ] ;
  memset ( dp, 0, sizeof ( *dp ) * ( W + 1 ) ) ;
  for ( int i = 0 ; i < n ; i ++ )
    for ( int j = W ; j >= 0 ; j -- )
        if ( j - wt [ i ] >= 0 )
            dp [ j ] = max ( dp [ j ], val [ i ] + dp [ j - wt [ i ] ] ) ;
  return dp [ W ] ;
}