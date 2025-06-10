public static int f_gold ( int [ ] arr , int n , int x , int y ) {
  int minDist = 2147483647 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( x == arr [ i ] && y == arr [ j ] || y == arr [ i ] && x == arr [ j ] ) && minDist > Math . abs ( i - j ) ) {
        minDist = Math . abs ( i - j ) ;
      }
    }
  }
  return minDist ;
}