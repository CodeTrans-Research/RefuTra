int f_gold ( int N, int insert, int remove, int copy ) {
  if ( N == 0 ) return 0;
  if ( N == 1 ) return insert;
  int dp [ ] = new int [ N + 1 ];
  for ( int i = 1;
  i <= N;
  i ++ ) {
    if ( i % 2 == 0 ) dp [ i ] = Math . min ( dp [ i - 1 ] + insert, dp [ i / 2 ] + copy );
    else dp [ i ] = Math . min ( dp [ i - 1 ] + insert, dp [ ( i + 1 ) / 2 ] + copy + remove );
  }
  return dp [ N ];
}