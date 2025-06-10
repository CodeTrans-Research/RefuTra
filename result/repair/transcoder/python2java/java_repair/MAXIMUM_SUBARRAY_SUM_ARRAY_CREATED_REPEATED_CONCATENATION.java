  int f_gold ( int [ ] a , int n , int k ) {
  int maxSoFar = - 2147483648 ;
  int maxEndingHere = 0 ;
  for ( int i = 0 ;
  i < n * k ;
  i ++ ) {
    maxEndingHere = maxEndingHere + a [ i % n ] ;
    if ( maxSoFar < maxEndingHere ) maxSoFar = maxEndingHere ;
    if ( maxEndingHere < 0 ) maxEndingHere = 0 ;
  }
  return maxSoFar ;
}

