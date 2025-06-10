String f_gold ( char [ ] str ) {
  Stack < Character > st = new Stack < > ( ) ;
  for ( int i = 0 ;
  i < str . length ;
  i ++ ) st . push ( str [ i ] ) ;
  for ( int i = 0 ;
  i < str . length ;
  i ++ ) {
    str [ i ] = st . peek ( ) ;
    st . pop ( ) ;
  }
  return String . valueOf ( str ) ;
}