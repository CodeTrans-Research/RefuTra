boolean f_gold ( String s ) {
  int l = s . length ( ) ;
  if ( l % 2 == 1 ) {
    return false ;
  }
  int i = 0 ;
  int j = l - 1 ;
  while ( i < j ) {
    if ( s . charAt ( i ) != 'a' || s . charAt ( j ) != 'b' ) {
      return false ;
    }
    i ++ ;
    j -- ;
  }
  return true ;
}