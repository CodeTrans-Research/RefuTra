public static int f_gold ( String s , String t ) {
  int count = 0 ;
  for ( int i = 0 ;
  ;
  i ++ ) {
    if ( ( count == s . length ( ) ) && ( i < t . length ( ) ) ) break ;
    if ( ( t . charAt ( i ) == s . charAt ( count ) ) && ( i < t . length ( ) ) ) count = count + 1 ;
  }
  return count ;
}
