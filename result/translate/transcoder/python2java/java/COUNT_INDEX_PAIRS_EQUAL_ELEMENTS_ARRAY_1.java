public static int f_gold ( int [ ] arr , int n ) {
  Map < Integer , Integer > mp = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] < mp . keySet ( ) . size ( ) ) {
      mp . put ( arr [ i ] , 1 ) ;
    }
    else {
      mp . put ( arr [ i ] , 1 ) ;
    }
  }
  int ans = 0 ;
  for ( Integer it : mp . keySet ( ) ) {
    int count = mp . get ( it ) ;
    ans += ( count * ( count - 1 ) ) / 2 ;
  }
  return ans ;
}
