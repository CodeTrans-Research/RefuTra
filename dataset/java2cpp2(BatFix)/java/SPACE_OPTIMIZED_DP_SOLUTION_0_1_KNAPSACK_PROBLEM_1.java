int f_gold ( int val [ ], int wt [ ], int n, int W ) {
  int [ ] dp = new int [ W + 1 ];
  Arrays . fill ( dp, 0 );
  for ( int i = 0;
  i < n;
  i ++ ) for ( int j = W;
  j >= wt [ i ];
  j -- ) dp [ j ] = Math . max ( dp [ j ], val [ i ] + dp [ j - wt [ i ] ] );
  return dp [ W ];
}