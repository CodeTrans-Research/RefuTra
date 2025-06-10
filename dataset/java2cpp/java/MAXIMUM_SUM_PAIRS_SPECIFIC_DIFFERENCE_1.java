int f_gold ( int arr [ ] , int N , int k ) {
  int maxSum = 0 ;
  Arrays . sort ( arr ) ;
  for ( int i = N - 1 ;
  i > 0 ;
  -- i ) {
    if ( arr [ i ] - arr [ i - 1 ] < k ) {
      maxSum += arr [ i ] ;
      maxSum += arr [ i - 1 ] ;
      -- i ;
    }
  }
  return maxSum ;
}