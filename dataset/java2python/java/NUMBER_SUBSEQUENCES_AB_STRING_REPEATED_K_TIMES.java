int f_gold ( String s , int K ) {
  int n = s . length ( ) ;
  int C = 0 , c1 = 0 , c2 = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( s . charAt ( i ) == 'a' ) c1 ++ ;
    if ( s . charAt ( i ) == 'b' ) {
      c2 ++ ;
      C += c1 ;
    }
  }
  return C * K + ( K * ( K - 1 ) / 2 ) * c1 * c2 ;
}