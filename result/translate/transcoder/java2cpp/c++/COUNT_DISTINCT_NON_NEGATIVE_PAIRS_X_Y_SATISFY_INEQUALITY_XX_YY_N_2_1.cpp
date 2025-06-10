int f_gold ( int n ) {
  int x = 0 , y_count , res = 0 ;
  for ( y_count = 0 ;
  y_count * y_count < n ;
  y_count ++ ) ;
  while ( y_count != 0 ) {
    res += y_count ;
    x ++ ;
    while ( y_count != 0 && ( x * x + ( y_count - 1 ) * ( y_count - 1 ) >= n ) ) {
      y_count -- ;
    }
  }
  return res ;
}