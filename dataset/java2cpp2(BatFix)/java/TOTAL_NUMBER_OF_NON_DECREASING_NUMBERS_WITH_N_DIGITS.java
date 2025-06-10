int f_gold ( int n ) {
  int dp [ ] [ ] = new int [ 10 ] [ n + 1 ];
  for ( int i = 0;
  i < 10;
  i ++ ) dp [ i ] [ 1 ] = 1;
  for ( int digit = 0;
  digit <= 9;
  digit ++ ) {
    for ( int len = 2;
    len <= n;
    len ++ ) {
      for ( int x = 0;
      x <= digit;
      x ++ ) dp [ digit ] [ len ] += dp [ x ] [ len - 1 ];
    }
  }
  int count = 0;
  for ( int i = 0;
  i < 10;
  i ++ ) count += dp [ i ] [ n ];
  return count;
}