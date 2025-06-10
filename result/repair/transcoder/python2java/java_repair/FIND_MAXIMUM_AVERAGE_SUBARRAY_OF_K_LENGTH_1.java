  int f_gold ( int [ ] arr , int n , int k ) {
  if ( k > n ) return - 1 ;
  int sum = arr [ 0 ] ;
  for ( int i = 1 ;
  i < k ;
  i ++ ) sum += arr [ i ] ;
  int maxSum = sum ;
  int maxEnd = k - 1 ;
  for ( int i = k ;
  i < n ;
  i ++ ) {
    sum = sum + arr [ i ] - arr [ i - k ] ;
    if ( sum > maxSum ) {
      maxSum = sum ;
      maxEnd = i ;
    }
  }
  return maxEnd - k + 1 ;
}

