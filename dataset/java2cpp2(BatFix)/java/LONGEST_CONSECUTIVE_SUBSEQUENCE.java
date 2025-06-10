int f_gold ( int arr [ ], int n ) {
  HashSet < Integer > S = new HashSet < Integer > ( );
  int ans = 0;
  for ( int i = 0;
  i < n;
  ++ i ) S . add ( arr [ i ] );
  for ( int i = 0;
  i < n;
  ++ i ) {
    if ( ! S . contains ( arr [ i ] - 1 ) ) {
      int j = arr [ i ];
      while ( S . contains ( j ) ) j ++;
      if ( ans < j - arr [ i ] ) ans = j - arr [ i ];
    }
  }
  return ans;
}