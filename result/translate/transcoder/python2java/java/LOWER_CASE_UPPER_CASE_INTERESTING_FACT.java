public static String f_gold ( String in ) {
  for ( int i = 0 ;
  i < in . length ( ) ;
  i ++ ) {
    if ( 'a' <= in . charAt ( i ) && in . charAt ( i ) <= 'z' ) {
      in . setCharAt ( i , Character . toLowerCase ( in . charAt ( i ) ) ) ;
    }
  }
  return in ;
}