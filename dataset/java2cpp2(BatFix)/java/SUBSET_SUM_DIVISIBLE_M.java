boolean f_gold ( int arr [ ], int n, int m ) {
  if ( n > m ) return true;
  boolean DP [ ] = new boolean [ m ];
  Arrays . fill ( DP, false );
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( DP [ 0 ] ) return true;
    boolean temp [ ] = new boolean [ m ];
    Arrays . fill ( temp, false );
    for ( int j = 0;
    j < m;
    j ++ ) {
      if ( DP [ j ] == true ) {
        if ( DP [ ( j + arr [ i ] ) % m ] == false ) temp [ ( j + arr [ i ] ) % m ] = true;
      }
    }
    for ( int j = 0;
    j < m;
    j ++ ) if ( temp [ j ] ) DP [ j ] = true;
    DP [ arr [ i ] % m ] = true;
  }
  return DP [ 0 ];
}