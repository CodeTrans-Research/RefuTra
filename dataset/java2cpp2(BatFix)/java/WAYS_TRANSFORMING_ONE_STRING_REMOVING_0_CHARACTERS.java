int f_gold ( String a, String b ) {
  int n = a . length ( ), m = b . length ( );
  if ( m == 0 ) {
    return 1;
  }
  int dp [ ] [ ] = new int [ m + 1 ] [ n + 1 ];
  for ( int i = 0;
  i < m;
  i ++ ) {
    for ( int j = i;
    j < n;
    j ++ ) {
      if ( i == 0 ) {
        if ( j == 0 ) {
          dp [ i ] [ j ] = ( a . charAt ( j ) == b . charAt ( i ) ) ? 1 : 0;
        }
        else if ( a . charAt ( j ) == b . charAt ( i ) ) {
          dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + 1;
        }
        else {
          dp [ i ] [ j ] = dp [ i ] [ j - 1 ];
        }
      }
      else if ( a . charAt ( j ) == b . charAt ( i ) ) {
        dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + dp [ i - 1 ] [ j - 1 ];
      }
      else {
        dp [ i ] [ j ] = dp [ i ] [ j - 1 ];
      }
    }
  }
  return dp [ m - 1 ] [ n - 1 ];
}