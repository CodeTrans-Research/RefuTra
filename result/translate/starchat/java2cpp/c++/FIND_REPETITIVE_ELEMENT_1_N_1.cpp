int f_gold ( int arr [ ] : n ) {
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) sum += arr [ i ] ;
  return sum - ( ( ( n - 1 ) * n ) / 2 ) ;
}