int f_gold ( int arr [ ] , int n ) {
  HashSet < Integer > s = new HashSet < > ( ) ;
  int count = 0 , maxm = Integer . MIN_VALUE , minm = Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    s . add ( arr [ i ] ) ;
    if ( arr [ i ] < minm ) minm = arr [ i ] ;
    if ( arr [ i ] > maxm ) maxm = arr [ i ] ;
  }
  for ( int i = minm ;
  i <= maxm ;
  i ++ ) if ( ! s . contains ( i ) ) count ++ ;
  return count ;
}