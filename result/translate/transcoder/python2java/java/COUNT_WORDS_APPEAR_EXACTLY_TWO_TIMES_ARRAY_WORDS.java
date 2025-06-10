public static int f_gold ( String stri [ ] , int n ) {
  Map < String , Integer > m = new HashMap < String , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    m . put ( stri [ i ] , m . get ( stri [ i ] ) + 1 ) ;
  }
  int res = 0 ;
  for ( int i = 0 ;
  i < m . values ( ) . length ;
  i ++ ) {
    if ( m . get ( i ) == 2 ) {
      res ++ ;
    }
  }
  return res ;
}
