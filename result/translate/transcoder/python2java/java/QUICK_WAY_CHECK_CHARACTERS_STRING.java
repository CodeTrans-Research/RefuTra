public static boolean f_gold ( String s ) {
  int n = s . length ( ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( s . charAt ( i ) != s . charAt ( 0 ) ) {
      return false ;
    }
  }
  return true ;
}
