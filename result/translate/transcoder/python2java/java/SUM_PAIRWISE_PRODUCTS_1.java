static double f_gold ( int n ) {
  int multiTerms = n * ( n + 1 ) / 2 ;
  double sm = multiTerms ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    multiTerms = multiTerms - ( i - 1 ) ;
    sm = sm + multiTerms * i ;
  }
  return sm ;
}
