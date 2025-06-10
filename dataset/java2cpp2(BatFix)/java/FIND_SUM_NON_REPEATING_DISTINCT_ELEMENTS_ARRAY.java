int f_gold ( int arr [ ], int n ) {
  int sum = 0;
  HashSet < Integer > s = new HashSet < Integer > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( ! s . contains ( arr [ i ] ) ) {
      sum += arr [ i ];
      s . add ( arr [ i ] );
    }
  }
  return sum;
}