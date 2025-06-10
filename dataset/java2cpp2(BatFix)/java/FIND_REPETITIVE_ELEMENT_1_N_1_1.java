int f_gold ( int arr [ ], int n ) {
  HashSet < Integer > s = new HashSet < Integer > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( s . contains ( arr [ i ] ) ) return arr [ i ];
    s . add ( arr [ i ] );
  }
  return - 1;
}