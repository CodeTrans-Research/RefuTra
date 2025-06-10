boolean f_gold ( int pre [ ], int n ) {
  Stack < Integer > s = new Stack < Integer > ( );
  int root = Integer . MIN_VALUE;
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( pre [ i ] < root ) {
      return false;
    }
    while ( ! s . empty ( ) && s . peek ( ) < pre [ i ] ) {
      root = s . peek ( );
      s . pop ( );
    }
    s . push ( pre [ i ] );
  }
  return true;
}