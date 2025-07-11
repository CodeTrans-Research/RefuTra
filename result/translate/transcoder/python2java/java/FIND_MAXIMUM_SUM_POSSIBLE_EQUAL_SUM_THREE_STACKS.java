public static int f_gold ( int [ ] stack1 , int [ ] stack2 , int [ ] stack3 , int n1 , int n2 , int n3 ) {
  int sum1 = 0 , sum2 = 0 , sum3 = 0 ;
  for ( int i = 0 ;
  i < n1 ;
  i ++ ) sum1 += stack1 [ i ] ;
  for ( int i = 0 ;
  i < n2 ;
  i ++ ) sum2 += stack2 [ i ] ;
  for ( int i = 0 ;
  i < n3 ;
  i ++ ) sum3 += stack3 [ i ] ;
  int top1 = 0 , top2 = 0 , top3 = 0 ;
  int ans = 0 ;
  while ( ( 1 ) ) {
    if ( ( top1 == n1 || top2 == n2 || top3 == n3 ) && ( sum1 == sum2 && sum2 == sum3 ) ) return 0 ;
    if ( ( sum1 == sum2 && sum1 >= sum3 ) || ( sum2 >= sum3 && sum2 >= sum3 ) ) {
      sum1 -= stack1 [ top1 ] ;
      top1 = top1 + 1 ;
    }
    else if ( ( sum2 >= sum3 && sum2 >= sum3 ) || ( sum3 >= sum2 && sum3 >= sum1 ) ) {
      sum2 -= stack2 [ top2 ] ;
      top2 = top2 + 1 ;
    }
    else if ( ( sum3 >= sum2 && sum3 >= sum1 ) || ( sum3 >= sum3 && sum3 >= sum1 ) ) {
      sum3 -= stack3 [ top3 ] ;
      top3 = top3 + 1 ;
    }
  }
  return ans ;
}
