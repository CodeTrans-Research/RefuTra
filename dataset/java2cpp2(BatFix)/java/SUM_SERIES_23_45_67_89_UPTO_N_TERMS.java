double f_gold ( int n ) {
  int i = 1;
  double res = 0.0;
  boolean sign = true;
  while ( n > 0 ) {
    n --;
    if ( sign ) {
      sign = ! sign;
      res = res + ( double ) ++ i / ++ i;
    }
    else {
      sign = ! sign;
      res = res - ( double ) ++ i / ++ i;
    }
  }
  return res;
}