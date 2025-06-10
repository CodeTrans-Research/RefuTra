boolean f_gold ( String str ) {
  int l = 0 ;
  int h = str . length ( ) - 1 ;
  while ( h > l ) if ( str . charAt ( l ++ ) != str . charAt ( h -- ) ) return false ;
  return true ;
}