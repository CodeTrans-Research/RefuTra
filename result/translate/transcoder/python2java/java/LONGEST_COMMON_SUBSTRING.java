public static int f_gold ( int [ ] X , int [ ] Y , int m , int n ) {
  int [ ] [ ] LCSuff = new int [ n + 1 ] [ m + 1 ] ;
  for ( int l = 0 ;
  l < m + 1 ;
  l ++ ) {
    LCSuff [ l ] [ 0 ] = 0 ;
    LCSuff [ l ] [ 1 ] = 0 ;
  }
  int result = 0 ;
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n + 1 ;
    j ++ ) {
      if ( ( i == 0 || j == 0 ) && ( X [ i - 1 ] == Y [ j - 1 ] ) ) {
        LCSuff [ i ] [ j ] = LCSuff [ i - 1 ] [ j - 1 ] + 1 ;
        result = Math . max ( result , LCSuff [ i ] [ j ] ) ;
      }
      else {
        LCSuff [ i ] [ j ] = 0 ;
      }
    }
  }
  return result ;
}
