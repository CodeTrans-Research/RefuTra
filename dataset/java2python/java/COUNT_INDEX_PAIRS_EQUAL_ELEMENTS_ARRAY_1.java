int f_gold ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > hm = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( hm . containsKey ( arr [ i ] ) ) hm . put ( arr [ i ] , hm . get ( arr [ i ] ) + 1 ) ;
    else hm . put ( arr [ i ] , 1 ) ;
  }
  int ans = 0 ;
  for ( Map . Entry < Integer , Integer > it : hm . entrySet ( ) ) {
    int count = it . getValue ( ) ;
    ans += ( count * ( count - 1 ) ) / 2 ;
  }
  return ans ;
}