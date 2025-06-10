int f_gold ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > um = new HashMap < Integer , Integer > ( ) ;
  int sum = 0 , maxLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += arr [ i ] == 0 ? - 1 : 1 ;
    if ( sum == 1 ) maxLen = i + 1 ;
    else if ( ! um . containsKey ( sum ) ) um . put ( sum , i ) ;
    if ( um . containsKey ( sum - 1 ) ) {
      if ( maxLen < ( i - um . get ( sum - 1 ) ) ) maxLen = i - um . get ( sum - 1 ) ;
    }
  }
  return maxLen ;
}