public static double f_gold ( double A , int N ) {
  Random random = new Random ( 1 ) ;
  double xPre = random . nextInt ( 101 ) % 10 ;
  double eps = 0.001 ;
  double delX = 2147483647 ;
  double xK = 0.0 ;
  while ( ( delX > eps ) && ( delX > 0 ) ) {
    xK = ( ( N - 1.0 ) * xPre + A / Math . pow ( xPre , N - 1 ) ) / N ;
    delX = Math . abs ( xK - xPre ) ;
    xPre = xK ;
  }
  return xK ;
}