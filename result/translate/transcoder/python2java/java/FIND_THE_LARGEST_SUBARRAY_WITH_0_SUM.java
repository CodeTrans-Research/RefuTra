public static int f_gold ( int [ ] arr , int n ) {
  int maxLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int currSum = 0 ;
    for ( int j = i ;
    j < n ;
    j ++ ) {
      currSum += arr [ j ] ;
      if ( currSum == 0 ) maxLen = Math . max ( maxLen , j - i + 1 ) ;
    }
  }
  return maxLen ;
}