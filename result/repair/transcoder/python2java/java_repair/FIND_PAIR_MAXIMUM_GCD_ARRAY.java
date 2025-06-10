  int f_gold ( int [ ] arr , int n ) {
  int high = 0 ;
  int i = 0 ;
  while ( i < n ) {
    high = Math . max ( high , arr [ i ] ) ;
    i = i + 1 ;
  }
  int [ ] divisors = new int [ high + 1 ] ;
  divisors [ 0 ] = 0 ;
  i = 0 ;
  while ( i < n ) {
    int j = 1 ;
    while ( j <= Math . sqrt ( arr [ i ] ) ) {
      if ( arr [ i ] % j == 0 ) {
        divisors [ j ] = divisors [ j ] + 1 ;
        if ( ( j != arr [ i ] / j ) && ( j != arr [ i ] / j ) ) {
          divisors [ arr [ i ] / j ] = divisors [ arr [ i ] / j ] + 1 ;
        }
      }
      j = j + 1 ;
    }
    i = i + 1 ;
  }
  i = high ;
  while ( i >= 1 ) {
    if ( divisors [ i ] > 1 ) {
      return i ;
    }
    i = i - 1 ;
  }
  return 1 ;
}
