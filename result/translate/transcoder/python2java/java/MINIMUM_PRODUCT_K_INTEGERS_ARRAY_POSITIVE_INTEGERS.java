public static int f_gold ( int [ ] arr , int n , int k ) {
  int [ ] pq = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    heapify ( pq , arr [ i ] ) ;
  }
  int count = 0 ;
  int ans = 1 ;
  while ( pq != null && count < k ) {
    ans += heapify ( pq ) ;
    count ++ ;
  }
  return ans ;
}