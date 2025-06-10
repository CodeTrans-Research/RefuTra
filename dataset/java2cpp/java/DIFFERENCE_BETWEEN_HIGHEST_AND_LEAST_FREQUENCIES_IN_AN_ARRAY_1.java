int f_gold ( int arr [ ] , int n ) {
  Map < Integer , Integer > mp = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( mp . containsKey ( arr [ i ] ) ) {
      mp . put ( arr [ i ] , mp . get ( arr [ i ] ) + 1 ) ;
    }
    else {
      mp . put ( arr [ i ] , 1 ) ;
    }
  }
  int max_count = 0 , min_count = n ;
  for ( Map . Entry < Integer , Integer > x : mp . entrySet ( ) ) {
    max_count = Math . max ( max_count , x . getValue ( ) ) ;
    min_count = Math . min ( min_count , x . getValue ( ) ) ;
  }
  return ( max_count - min_count ) ;
}