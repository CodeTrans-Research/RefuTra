char f_gold ( const char * str , int i ) {
  if ( str [ i ] == '\0' ) return 0 ;
  if ( isupper ( str [ i ] ) ) return str [ i ] ;
  return f_gold ( str , i + 1 ) ;
}