private  int f_gold ( int W, int n, int [ ] val, int [ ] wt ) {
  int dp [ ] = new int [ W + 1 ];
  for ( int i = 0;
  i <= W;
  i ++ ) {
    for ( int j = 0;
    j < n;
    j ++ ) {
      if ( wt [ j ] <= i ) {
        dp [ i ] = max ( dp [ i ], dp [ i - wt [ j ] ] + val [ j ] );
      }
    }
  }
  return dp [ W ];
}