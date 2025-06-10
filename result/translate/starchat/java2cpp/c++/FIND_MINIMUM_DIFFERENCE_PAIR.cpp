int f_gold ( int arr [ ] [ ] , int n ) {
  int diff = INT_MAX ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = 0 ;
  j < n ;
  j ++ ) if ( abs ( arr [ i ] [ j ] - arr [ i + 1 ] [ j ] ) < diff ) diff = abs ( arr [ i ] [ j ] - arr [ i + 1 ] [ j ] ) ;
  return diff ;
}