char f_gold ( const char * str ) {
  for ( int i = 0 ;
  i < strlen ( str ) ;
  i ++ ) if ( isupper ( str [ i ] ) ) return str [ i ] ;
  return 0 ;
}