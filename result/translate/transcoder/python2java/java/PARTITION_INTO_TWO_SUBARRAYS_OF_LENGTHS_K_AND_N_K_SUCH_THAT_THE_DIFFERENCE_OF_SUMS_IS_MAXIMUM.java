public static int f_gold ( int [ ] arr , int N , int k ) {
  int S = 0 ;
  int S1 = 0 ;
  int maxDifference = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    S += arr [ i ] ;
  }
  Arrays . sort ( arr ) ;
  int M = Math . max ( k , N - k ) ;
  for ( int i = 0 ;
  i < M ;
  i ++ ) {
    S1 += arr [ i ] ;
  }
  maxDifference = S1 - ( S - S1 ) ;
  return maxDifference ;
}