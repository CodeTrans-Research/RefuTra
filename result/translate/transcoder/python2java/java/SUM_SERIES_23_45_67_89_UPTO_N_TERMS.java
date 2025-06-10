public static double f_gold ( int n ) {
  int i = 1 ;
  double res = 0.0 ;
  ;
  boolean sign = true ;
  while ( ( n > 0 ) && ( ( sign ) || ( ( i - 1 ) < n ) ) ) {
    n = n - 1 ;
    if ( ( sign ) || ( ( i - 1 ) < n ) ) {
      sign = false ;
      res = res + ( i + 1 ) / ( i + 2 ) ;
      i = i + 2 ;
    }
    else {
      sign = true ;
      res = res - ( i + 1 ) / ( i + 2 ) ;
      i = i + 2 ;
    }
  }
  return res ;
}
