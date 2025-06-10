public static char fGolders ( String strA , String strB ) {
  int res = 0 ;
  for ( int i = 0 ;
  i != strA . length ( ) ;
  i ++ ) {
    res = res ^ ( ( char ) ( strA . charAt ( i ) ) ) ;
  }
  for ( int i = 0 ;
  i != strB . length ( ) ;
  i ++ ) {
    res = res ^ ( ( char ) ( strB . charAt ( i ) ) ) ;
  }
  return ( ( char ) ( res ) ) ;
  ;
}
