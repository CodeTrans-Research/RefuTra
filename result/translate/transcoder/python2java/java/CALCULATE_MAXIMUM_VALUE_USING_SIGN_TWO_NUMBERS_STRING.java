public static int f_gold ( String str ) {
  int res = ( int ) ( str . charAt ( 0 ) - 48 ) ;
  for ( int i = 1 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( ( str . charAt ( i ) == '0' || str . charAt ( i ) == '1' || res < 2 ) && ( i < str . length ( ) - 1 ) ) {
      res += ( int ) ( str . charAt ( i ) - 48 ) ;
    }
    else {
      res += ( int ) ( str . charAt ( i ) - 48 ) ;
    }
  }
  return res ;
}