public static String f_gold ( String Str ) {
  int Len = Str . length ( ) ;
  char [ ] res = new char [ Len ] ;
  int index = 0 ;
  int i = 0 ;
  int [ ] s = new int [ Len ] ;
  s [ 0 ] = 0 ;
  while ( ( i < Len ) && ( i > 0 ) ) {
    if ( ( Str . charAt ( i ) == '+' ) ) {
      if ( ( s [ s . length - 1 ] == 1 ) || ( s [ s . length - 1 ] == 0 ) ) {
        res [ index ] = '-' ;
        index ++ ;
      }
      if ( ( s [ s . length - 1 ] == 0 ) || ( s [ s . length - 1 ] == 1 ) ) {
        res [ index ] = '+' ;
        index ++ ;
      }
    }
    else if ( ( Str . charAt ( i ) == '-' ) ) {
      if ( ( s [ s . length - 1 ] == 1 ) || ( s [ s . length - 1 ] == 0 ) ) {
        res [ index ] = '+' ;
        index ++ ;
      }
      else if ( ( s [ s . length - 1 ] == 0 ) || ( s [ s . length - 1 ] == 1 ) ) {
        res [ index ] = '-' ;
        index ++ ;
      }
    }
    else if ( ( Str . charAt ( i ) == '(' ) && i > 0 ) ) {
      if ( ( Str . charAt ( i - 1 ) == '-' ) ) {
        int x = 0 == ( s [ s . length - 1 ] == 1 ) ? 1 : 0 ;
        s [ s . length - 1 ] = x ;
      }
      else if ( ( Str . charAt ( i - 1 ) == '+' ) ) {
        s [ s . length - 1 ] = s [ s . length - 1 ] ;
      }
    }
    else if ( ( Str . charAt ( i ) == ')' ) ) {
      s [ s . length - 1 ] = 0 ;
    }
    else {
      res [ index ] = Str . charAt ( i ) ;
      index ++ ;
    }
    i ++ ;
  }
  return new String ( res ) ;
}