int f_gold ( int arr [ ], int n ) {
  Set < Integer > s = new HashSet < > ( );
  int first = 0, second = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( ! s . contains ( arr [ i ] ) ) {
      s . add ( arr [ i ] );
      continue;
    }
    if ( arr [ i ] > first ) {
      second = first;
      first = arr [ i ];
    }
    else if ( arr [ i ] > second ) second = arr [ i ];
  }
  return ( first * second );
}