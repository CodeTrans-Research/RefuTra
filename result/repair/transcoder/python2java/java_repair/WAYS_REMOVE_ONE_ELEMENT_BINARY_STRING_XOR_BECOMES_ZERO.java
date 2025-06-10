  int f_gold ( String str ) {
  int oneCount = 0 ;
  int zeroCount = 0 ;
  int n = str . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i += 1 ) {
    if ( str.charAt( i ) == '1' ) {
      oneCount ++ ;
    }
    else {
      zeroCount ++ ;
    }
  }
  if ( oneCount % 2 == 0 ) {
    return zeroCount ;
  }
  return oneCount ;
}

