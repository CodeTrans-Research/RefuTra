public static boolean fGoldenArray ( int [ ] arr , int n , int k ) {
  TreeMap < Integer , Integer > mp = new TreeMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    mp . put ( arr [ i ] , 0 ) ;
  }
  for ( Map . Entry < Integer , Integer > entry : mp . entrySet ( ) ) {
    if ( entry . getValue ( ) > 2 * k ) {
      return false ;
    }
  }
  return true ;
}