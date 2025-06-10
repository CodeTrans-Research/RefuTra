public static int f_gold ( int [ ] arr , int n ) {
  TreeMap < Integer , Integer > Hash = new TreeMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    Hash . put ( arr [ i ] , 0 ) ;
  }
  int maxCount = 0 ;
  for ( int i = 0 ;
  i < Hash . size ( ) ;
  i ++ ) {
    if ( maxCount < Hash . get ( i ) ) {
      maxCount = Hash . get ( i ) ;
    }
  }
  return n - maxCount ;
}