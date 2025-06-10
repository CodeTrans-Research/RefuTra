int f_gold ( int arr [ ] [ ], int n, int m ) {
  int leftMax [ n ] [ m ] = { { 0 } } ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( i == 0 ) leftMax [ i ][ j ] = INT_MIN ;
      else leftMax [ i ][ j ] = max ( leftMax [ i - 1 ][ j ], arr [ i - 1 ][ j ] ) ;
    }
  }
  int rightMin = INT_MAX ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( leftMax [ i ][ j ] < arr [ i ][ j ] && rightMin > arr [ i ][ j ] ) return i ;
      rightMin = min ( rightMin, arr [ i ][ j ] ) ;
    }
  }
  return - 1 ;
}