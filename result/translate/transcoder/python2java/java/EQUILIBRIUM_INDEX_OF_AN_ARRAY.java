public static int f_gold ( int [ ] arr , int n ) {
  int leftsum ;
  int rightsum ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    leftsum = 0 ;
    rightsum = 0 ;
    for ( int j = 0 ;
    j < i ;
    j ++ ) leftsum += arr [ j ] ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) rightsum += arr [ j ] ;
    if ( leftsum == rightsum ) return i ;
  }
  return - 1 ;
}