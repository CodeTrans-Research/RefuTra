  double f_gold ( int n ) {
  if ( n % 2 != 0 ) return 0 ;
  double res = 1 ;
  for ( int i = 2 ;
  i <= ( int ) ( Math . sqrt ( n ) ) ;
  i ++ ) {
    int count = 0 ;
    double currSum = 1 ;
    double currTerm = 1 ;
    while ( ( n % i == 0 ) && ( n % i == 0 ) ) {
      count = count + 1 ;
      n = n / i ;
      if ( i == 2 && count == 1 ) currSum = 0 ;
      currTerm = currTerm * i ;
      currSum = currSum + currTerm ;
    }
    res = res * currSum ;
  }
  if ( n >= 2 ) res = res * ( 1 + n ) ;
  return res ;
}

