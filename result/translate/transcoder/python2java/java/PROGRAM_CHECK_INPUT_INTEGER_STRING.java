public static boolean f_gold ( String s ) {
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( s . charAt ( i ) . matches ( "[0-9]+" ) != true ) {
      return false ;
    }
  }
  return true ;
}
