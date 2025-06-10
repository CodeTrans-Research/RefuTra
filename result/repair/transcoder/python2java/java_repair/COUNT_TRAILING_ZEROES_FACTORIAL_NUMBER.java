  int f_gold ( int n ) {
  long count = 0 ;
  int i = 5 ;
  while (n/i>=1){
    count += ( int ) ( n / i ) ;
    i *= 5 ;
  }
  return ( int ) count ;
}

