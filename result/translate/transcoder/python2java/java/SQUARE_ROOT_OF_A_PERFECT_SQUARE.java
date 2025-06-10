public static double f_gold ( double n ) {
  double x = n ;
  double y = 1 ;
  double e = 0.000001 ;
  while ( ( x - y > e ) && ( y > n ) ) {
    x = ( x + y ) / 2 ;
    y = n / x ;
  }
  return x ;
}
