char f_gold ( string strA, string strB ) {
  int res = 0, i ;
  for ( i = 0 ;
  i < strA. length ( ) ;
  i ++ ) {
    res ^= strA. at ( i ) ;
  }
  for ( i = 0 ;
  i < strB. length ( ) ;
  i ++ ) {
    res ^= strB. at ( i ) ;
  }
  return ( ( char ) ( res ) ) ;
}