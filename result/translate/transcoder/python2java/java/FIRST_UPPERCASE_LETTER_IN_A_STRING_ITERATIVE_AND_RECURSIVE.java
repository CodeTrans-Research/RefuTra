public static int f_gold ( String str ) {
  for ( int i = 0 ;
  i != str . length ( ) ;
  i ++ ) {
    if ( ( str . charAt ( i ) ) . istitle ( ) ) {
      return i ;
    }
  }
  return 0 ;
}
