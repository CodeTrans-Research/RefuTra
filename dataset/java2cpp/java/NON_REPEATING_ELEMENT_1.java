int f_gold ( int arr [ ] , int n ) {
  Map < Integer , Integer > m = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( m . containsKey ( arr [ i ] ) ) {
      m . put ( arr [ i ] , m . get ( arr [ i ] ) + 1 ) ;
    }
    else {
      m . put ( arr [ i ] , 1 ) ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( m . get ( arr [ i ] ) == 1 ) return arr [ i ] ;
  return - 1 ;
}