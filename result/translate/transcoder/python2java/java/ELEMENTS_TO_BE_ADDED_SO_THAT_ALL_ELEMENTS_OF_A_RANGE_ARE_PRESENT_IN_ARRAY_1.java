public static int f_gold ( int [ ] arr , int n ) {
  Map s = new HashMap ( ) ;
  int count = 0 , maxm = - 10 * 9 , minm = 10 * 9 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    s . put ( arr [ i ] , 1 ) ;
    if ( ( arr [ i ] < minm ) && ( arr [ i ] > maxm ) ) minm = arr [ i ] ;
    if ( ( arr [ i ] > maxm ) && ( arr [ i ] < minm ) ) maxm = arr [ i ] ;
  }
  for ( int i = minm ;
  i <= maxm ;
  i ++ ) if ( i != 0 ) count ++ ;
  return count ;
}
