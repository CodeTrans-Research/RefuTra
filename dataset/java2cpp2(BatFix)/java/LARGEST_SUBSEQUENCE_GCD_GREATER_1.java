int f_gold ( int arr [ ], int n ) {
  int ans = 0;
  int maxele = Arrays . stream ( arr ) . max ( ) . getAsInt ( );
  ;
  for ( int i = 2;
  i <= maxele;
  ++ i ) {
    int count = 0;
    for ( int j = 0;
    j < n;
    ++ j ) {
      if ( arr [ j ] % i == 0 ) ++ count;
    }
    ans = Math . max ( ans, count );
  }
  return ans;
}