public static String f_gold ( String s ) {
  if ( ( s . equals ( " " ) ) || ( s . equals ( "a" ) ) ) return "a" ;
  int i = s . length ( ) - 1 ;
  while ( ( s . charAt ( i ) == 'z' ) && i >= 0 ) i -- ;
  if ( ( i == - 1 ) || ( s . charAt ( i ) == 'a' ) ) s = s + 'a' ;
  else s = s . substring ( 0 , i ) + ( char ) ( ( s . charAt ( i ) + 1 ) + s . charAt ( i + 1 ) ) ;
  return s ;
}