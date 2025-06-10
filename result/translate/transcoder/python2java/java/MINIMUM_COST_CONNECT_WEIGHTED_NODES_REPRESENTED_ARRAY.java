static double f_gold ( double [ ] a , int n ) {
  double mn = Double . MAX_VALUE ;
  double sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    mn = Math . min ( a [ i ] , mn ) ;
    sum += a [ i ] ;
  }
  return mn * ( sum - mn ) ;
}
