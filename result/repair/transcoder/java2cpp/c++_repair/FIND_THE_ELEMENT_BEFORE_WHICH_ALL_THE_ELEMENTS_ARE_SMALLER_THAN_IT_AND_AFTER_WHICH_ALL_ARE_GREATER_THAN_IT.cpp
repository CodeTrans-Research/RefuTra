int f_gold ( int arr [ ] , int n ) {
  int left_max [ n ] ;
  left_max [ 0 ] = INT_MIN ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    left_max [ i ] = max ( left_max [ i - 1 ] , arr [ i - 1 ] ) ;
  }
  int right_min = INT_MAX;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    if ( left_max [ i ] < arr [ i ] && right_min > arr [ i ] ) return i ;
    right_min = min ( right_min , arr [ i ] ) ;
  }
  return - 1 ;
}
