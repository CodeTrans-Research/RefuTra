char f_gold ( String str , int i ) {
  if ( str . charAt ( i ) == '\0' ) return 0 ;
  if ( Character . isUpperCase ( str . charAt ( i ) ) ) return str . charAt ( i ) ;
  return f_gold ( str , i + 1 ) ;
}