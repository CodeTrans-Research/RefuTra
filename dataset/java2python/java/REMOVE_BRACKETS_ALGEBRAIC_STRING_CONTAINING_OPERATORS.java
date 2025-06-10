String f_gold ( String str ) {
  int len = str . length ( ) ;
  char res [ ] = new char [ len ] ;
  int index = 0 , i = 0 ;
  Stack < Integer > s = new Stack < Integer > ( ) ;
  s . push ( 0 ) ;
  while ( i < len ) {
    if ( str . charAt ( i ) == '+' ) {
      if ( s . peek ( ) == 1 ) res [ index ++ ] = '-' ;
      if ( s . peek ( ) == 0 ) res [ index ++ ] = '+' ;
    }
    else if ( str . charAt ( i ) == '-' ) {
      if ( s . peek ( ) == 1 ) res [ index ++ ] = '+' ;
      else if ( s . peek ( ) == 0 ) res [ index ++ ] = '-' ;
    }
    else if ( str . charAt ( i ) == '(' && i > 0 ) {
      if ( str . charAt ( i - 1 ) == '-' ) {
        int x = ( s . peek ( ) == 1 ) ? 0 : 1 ;
        s . push ( x ) ;
      }
      else if ( str . charAt ( i - 1 ) == '+' ) s . push ( s . peek ( ) ) ;
    }
    else if ( str . charAt ( i ) == ')' ) s . pop ( ) ;
    else res [ index ++ ] = str . charAt ( i ) ;
    i ++ ;
  }
  return new String ( res ) ;
}