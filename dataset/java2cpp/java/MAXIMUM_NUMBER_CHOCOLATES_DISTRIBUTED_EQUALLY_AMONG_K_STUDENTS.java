int f_gold ( int arr [ ] , int n , int k ) {
  HashMap < Integer , Integer > um = new HashMap < Integer , Integer > ( ) ;
  int [ ] sum = new int [ n ] ;
  int curr_rem ;
  int maxSum = 0 ;
  sum [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) sum [ i ] = sum [ i - 1 ] + arr [ i ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    curr_rem = sum [ i ] % k ;
    if ( curr_rem == 0 ) {
      if ( maxSum < sum [ i ] ) maxSum = sum [ i ] ;
    }
    else if ( ! um . containsKey ( curr_rem ) ) um . put ( curr_rem , i ) ;
    else if ( maxSum < ( sum [ i ] - sum [ um . get ( curr_rem ) ] ) ) maxSum = sum [ i ] - sum [ um . get ( curr_rem ) ] ;
  }
  return ( maxSum / k ) ;
}