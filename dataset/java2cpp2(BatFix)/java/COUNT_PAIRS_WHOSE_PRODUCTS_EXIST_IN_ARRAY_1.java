int f_gold ( int arr [ ], int n ) {
  int result = 0;
  HashSet < Integer > Hash = new HashSet < > ( );
  for ( int i = 0;
  i < n;
  i ++ ) {
    Hash . add ( arr [ i ] );
  }
  for ( int i = 0;
  i < n;
  i ++ ) {
    for ( int j = i + 1;
    j < n;
    j ++ ) {
      int product = arr [ i ] * arr [ j ];
      if ( Hash . contains ( product ) ) {
        result ++;
      }
    }
  }
  return result;
}