public static String f_gold ( String s ) {
  int n = s . length ( ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( ( s . charAt ( i ) == s . charAt ( i - 1 ) ) && ( s . charAt ( i ) == s . charAt ( i - 1 ) || ( i + 1 < n && s . charAt ( i ) == s . charAt ( i + 1 ) ) ) ) {
      s . charAt ( i ) ++ ;
    }
    i ++ ;
  }
  return s ;
}