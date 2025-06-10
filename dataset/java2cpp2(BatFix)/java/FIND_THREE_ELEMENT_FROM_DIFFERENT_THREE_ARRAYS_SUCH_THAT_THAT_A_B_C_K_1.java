boolean f_gold ( int a1 [ ], int a2 [ ], int a3 [ ], int n1, int n2, int n3, int sum ) {
  HashSet < Integer > s = new HashSet < Integer > ( );
  for ( int i = 0;
  i < n1;
  i ++ ) {
    s . add ( a1 [ i ] );
  }
  ArrayList < Integer > al = new ArrayList < > ( s );
  for ( int i = 0;
  i < n2;
  i ++ ) {
    for ( int j = 0;
    j < n3;
    j ++ ) {
      if ( al . contains ( sum - a2 [ i ] - a3 [ j ] ) & al . indexOf ( sum - a2 [ i ] - a3 [ j ] ) != al . get ( al . size ( ) - 1 ) ) {
        return true;
      }
    }
  }
  return false;
}