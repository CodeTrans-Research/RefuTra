int f_gold ( int a [ ], int n ) {
  int total = 1 ;
  for ( int i = 2 ; i <= n ; i ++ ) {
    total += i ;
    total -= a [ i - 2 ] ;
  }
  return total ;
}