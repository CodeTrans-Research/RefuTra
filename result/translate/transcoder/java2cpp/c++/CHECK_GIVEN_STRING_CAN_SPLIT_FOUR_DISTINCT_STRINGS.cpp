bool f_gold ( string s ) {
  if ( s . size ( ) >= 10 ) return true ;
  for ( int i = 1 ;
  i < s . size ( ) ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < s . size ( ) ;
    j ++ ) {
      for ( int k = j + 1 ;
      k < s . size ( ) ;
      k ++ ) {
        string s1 , s2 , s3 , s4 ;
        try {
          s1 = s [ 0 ] ;
          s2 = s [ i ] ;
          s3 = s [ j ] ;
          s4 = s [ k ] ;
        }
        catch ( StringIndexOutOfBoundsException & ) {
        }
        if ( ! s1 . empty ( ) && ! s1 . empty ( ) && ! s1 . empty ( ) && ! s2 . empty ( ) && ! s2 . empty ( ) && ! s3 . empty ( ) && ! s3 . empty ( ) ) return true ;
      }
    }
  }
  return false ;
}