int f_gold ( String s , String t ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < t . length ( ) ;
  i ++ ) {
    if ( count == t . length ( ) ) break ;
    if ( t . charAt ( i ) == s . charAt ( count ) ) count ++ ;
  }
  return count ;
}