int f_gold ( string s , int n ) {
  int invalid_open_braces = 0 ;
  int invalid_close_braces = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( s [ i ] == '(' ) invalid_open_braces ++ ;
    else {
      if ( invalid_open_braces == 0 ) invalid_close_braces ++ ;
      else invalid_open_braces -- ;
    }
  }
  return ( n - ( invalid_open_braces + invalid_close_braces ) ) ;
}